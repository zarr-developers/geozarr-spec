#!/usr/bin/env python3
"""Generate GeoZarr conformance test datasets (Zarr v3).

See README.md for coverage table and implementer guidance.

Usage:
    python generate_datasets.py            # generate + manifest
    python generate_datasets.py --verify   # generate + manifest + self-check

Requires: zarr>=3.0, numpy
"""

import json
import shutil
import sys
from pathlib import Path

import numpy as np
import zarr

# ---------------------------------------------------------------------------
# Convention metadata (const values must match upstream JSON schemas)
# ---------------------------------------------------------------------------

PROJ_CONVENTION = {
    # URLs use zarr-experimental per upstream schema.json const values.
    # Will change to zarr-conventions once geozarr-spec#126 settles.
    "schema_url": "https://raw.githubusercontent.com/zarr-experimental/geo-proj/refs/tags/v1/schema.json",
    "spec_url": "https://github.com/zarr-experimental/geo-proj/blob/v1/README.md",
    "uuid": "f17cb550-5864-4468-aeb7-f3180cfb622f",
    "name": "proj:",
    "description": "Coordinate reference system information for geospatial data",
}

SPATIAL_CONVENTION = {
    "schema_url": "https://raw.githubusercontent.com/zarr-conventions/spatial/refs/tags/v1/schema.json",
    "spec_url": "https://github.com/zarr-conventions/spatial/blob/v1/README.md",
    "uuid": "689b58e2-cf7b-45e0-9fff-9cfc0883d6b4",
    "name": "spatial:",
    "description": "Spatial coordinate information",
}

MULTISCALES_CONVENTION = {
    "schema_url": "https://raw.githubusercontent.com/zarr-conventions/multiscales/refs/tags/v1/schema.json",
    "spec_url": "https://github.com/zarr-conventions/multiscales/blob/v1/README.md",
    "uuid": "d35379db-88df-4056-af3a-620245f8e347",
    "name": "multiscales",
    "description": "Multiscale layout of zarr datasets",
}

# WKT2 string for EPSG:32610 (UTM Zone 10N)
WKT2_UTM10N = (
    'PROJCRS["WGS 84 / UTM zone 10N",'
    'BASEGEOGCRS["WGS 84",DATUM["World Geodetic System 1984",'
    'ELLIPSOID["WGS 84",6378137,298.257223563]],'
    'ID["EPSG",4326]],'
    'CONVERSION["UTM zone 10N",METHOD["Transverse Mercator"],'
    'PARAMETER["Latitude of natural origin",0],'
    'PARAMETER["Longitude of natural origin",-123],'
    'PARAMETER["Scale factor at natural origin",0.9996],'
    'PARAMETER["False easting",500000],'
    'PARAMETER["False northing",0]],'
    'CS[Cartesian,2],AXIS["easting",east],AXIS["northing",north],'
    'UNIT["metre",1],ID["EPSG",32610]]'
)

# PROJJSON for EPSG:3857 (Web Mercator)
PROJJSON_3857 = {
    "$schema": "https://proj.org/schemas/v0.7/projjson.schema.json",
    "type": "ProjectedCRS",
    "name": "WGS 84 / Pseudo-Mercator",
    "base_crs": {
        "name": "WGS 84",
        "datum": {
            "type": "GeodeticReferenceFrame",
            "name": "World Geodetic System 1984",
            "ellipsoid": {
                "name": "WGS 84",
                "semi_major_axis": 6378137,
                "inverse_flattening": 298.257223563,
            },
        },
        "coordinate_system": {
            "subtype": "ellipsoidal",
            "axis": [
                {
                    "name": "Latitude",
                    "abbreviation": "lat",
                    "direction": "north",
                    "unit": "degree",
                },
                {
                    "name": "Longitude",
                    "abbreviation": "lon",
                    "direction": "east",
                    "unit": "degree",
                },
            ],
        },
        "id": {"authority": "EPSG", "code": 4326},
    },
    "conversion": {
        "name": "Popular Visualisation Pseudo-Mercator",
        "method": {
            "name": "Popular Visualisation Pseudo Mercator",
            "id": {"authority": "EPSG", "code": 1024},
        },
        "parameters": [
            {"name": "Latitude of natural origin", "value": 0, "unit": "degree"},
            {"name": "Longitude of natural origin", "value": 0, "unit": "degree"},
            {"name": "False easting", "value": 0, "unit": "metre"},
            {"name": "False northing", "value": 0, "unit": "metre"},
        ],
    },
    "coordinate_system": {
        "subtype": "Cartesian",
        "axis": [
            {
                "name": "Easting",
                "abbreviation": "X",
                "direction": "east",
                "unit": "metre",
            },
            {
                "name": "Northing",
                "abbreviation": "Y",
                "direction": "north",
                "unit": "metre",
            },
        ],
    },
    "id": {"authority": "EPSG", "code": 3857},
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent


def clean_and_create(path: Path) -> Path:
    """Remove existing store and ensure parent directories exist."""
    if path.exists():
        shutil.rmtree(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def gradient_data(shape, dtype="uint8", band_offset=0):
    """Deterministic gradient scaled to dtype range.

    2D: pixel[r,c] = ((r * W + c) / (H * W - 1)) * max_val
    3D: pixel[k,r,c] = clip(pixel[r,c] + k * band_offset, min, max)
    """
    h, w = shape[-2], shape[-1]
    n = h * w
    ramp = np.arange(n, dtype=np.float64) / max(n - 1, 1)
    if np.issubdtype(np.dtype(dtype), np.integer):
        info = np.iinfo(np.dtype(dtype))
        ramp = (ramp * info.max).astype(dtype)
    else:
        ramp = ramp.astype(dtype)
    plane = ramp.reshape(h, w)
    if len(shape) > 2:
        slices = []
        for k in range(shape[0]):
            if band_offset and np.issubdtype(np.dtype(dtype), np.integer):
                shifted = np.clip(
                    plane.astype(np.int64) + k * band_offset,
                    np.iinfo(np.dtype(dtype)).min,
                    np.iinfo(np.dtype(dtype)).max,
                ).astype(dtype)
                slices.append(shifted)
            else:
                slices.append(plane + k * band_offset)
        return np.stack(slices, axis=0)
    return plane


def downsample(data, factor):
    """Block-average a 2D array by integer factor."""
    h, w = data.shape
    return data.reshape(h // factor, factor, w // factor, factor).mean(axis=(1, 3))


def make_array(
    group,
    name,
    shape,
    dtype="uint8",
    chunks=None,
    fill_value=0,
    data=None,
    dim_names=("y", "x"),
):
    """Create a Zarr v3 array with gradient data (or explicit data)."""
    if chunks is None:
        chunks = shape
    arr = group.create_array(
        name,
        shape=shape,
        chunks=chunks,
        dtype=dtype,
        fill_value=fill_value,
        dimension_names=list(dim_names),
    )
    arr[:] = data if data is not None else gradient_data(shape, dtype)
    return arr


def patch_attrs(zarr_json_path: Path, attrs: dict):
    """Merge attrs into an existing zarr.json's attributes."""
    meta = json.loads(zarr_json_path.read_text())
    meta.setdefault("attributes", {}).update(attrs)
    zarr_json_path.write_text(json.dumps(meta, indent=2) + "\n")


def add_consolidated_metadata(store_path: Path):
    """Inline all child zarr.json into root (Zarr v3 consolidated metadata)."""
    root_zj = store_path / "zarr.json"
    root_meta = json.loads(root_zj.read_text())
    metadata = {}
    for child_zj in sorted(store_path.rglob("zarr.json")):
        if child_zj == root_zj:
            continue
        rel = str(child_zj.parent.relative_to(store_path))
        metadata[rel] = json.loads(child_zj.read_text())
        # Ensure trailing newline (zarr library omits it)
        content = child_zj.read_text()
        if not content.endswith("\n"):
            child_zj.write_text(content + "\n")
    root_meta["consolidated_metadata"] = {
        "kind": "inline",
        "must_understand": False,
        "metadata": metadata,
    }
    root_zj.write_text(json.dumps(root_meta, indent=2) + "\n")


# ---------------------------------------------------------------------------
# Valid: CRS encodings (one per oneOf path)
# ---------------------------------------------------------------------------

CRS_DATASETS = [
    ("crs-epsg-4326", {"proj:code": "EPSG:4326"}),
    ("crs-wkt2", {"proj:wkt2": WKT2_UTM10N}),
    ("crs-projjson", {"proj:projjson": PROJJSON_3857}),
]


def gen_crs_variants(base: Path):
    """One dataset per CRS encoding: EPSG code, WKT2, PROJJSON."""
    for name, crs_attrs in CRS_DATASETS:
        p = clean_and_create(base / f"{name}.zarr")
        g = zarr.open_group(str(p), mode="w", zarr_format=3)
        make_array(g, "ar", (8, 8))
        attrs = {"zarr_conventions": [PROJ_CONVENTION]}
        attrs.update(crs_attrs)
        patch_attrs(p / "ar" / "zarr.json", attrs)
        add_consolidated_metadata(p)


def gen_crs_override(base: Path):
    """Group=4326, band2=32632. Tests both inheritance and override."""
    p = clean_and_create(base / "crs-override.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    make_array(g, "band1", (8, 8))
    make_array(g, "band2", (8, 8))
    patch_attrs(
        p / "zarr.json",
        {
            "zarr_conventions": [PROJ_CONVENTION],
            "proj:code": "EPSG:4326",
        },
    )
    patch_attrs(
        p / "band2" / "zarr.json",
        {
            "zarr_conventions": [PROJ_CONVENTION],
            "proj:code": "EPSG:32632",
        },
    )
    add_consolidated_metadata(p)


# ---------------------------------------------------------------------------
# Valid: spatial transform variations
# ---------------------------------------------------------------------------


def gen_spatial_north_up(base: Path):
    """North-up affine with bbox. Baseline spatial test."""
    p = clean_and_create(base / "spatial-north-up.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    make_array(g, "ar", (8, 8))
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [SPATIAL_CONVENTION, PROJ_CONVENTION],
            "spatial:dimensions": ["y", "x"],
            "spatial:transform_type": "affine",
            "spatial:transform": [1.25, 0.0, 0.0, 0.0, -1.25, 10.0],
            "spatial:bbox": [0.0, 0.0, 10.0, 10.0],
            "proj:code": "EPSG:4326",
        },
    )
    add_consolidated_metadata(p)


def gen_spatial_rotated(base: Path):
    """30-degree rotated grid in UTM (non-zero b, d coefficients).

    Intentionally omits spatial:transform_type to test default ("affine").
    Omits spatial:bbox - computing axis-aligned bbox for rotated grids is
    non-trivial and bbox is optional per the spatial convention.
    """
    p = clean_and_create(base / "spatial-rotated.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    make_array(g, "ar", (8, 8))
    cos30 = float(np.cos(np.deg2rad(30)))
    sin30 = float(np.sin(np.deg2rad(30)))
    res = 10.0
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [SPATIAL_CONVENTION, PROJ_CONVENTION],
            "spatial:dimensions": ["y", "x"],
            "spatial:transform": [
                round(cos30 * res, 6),
                round(-sin30 * res, 6),
                500000.0,
                round(sin30 * res, 6),
                round(-cos30 * res, 6),
                5000080.0,
            ],
            "proj:code": "EPSG:32632",
        },
    )
    add_consolidated_metadata(p)


def gen_spatial_pixel_is_point(base: Path):
    """Node (point) registration - 9x9 for 8-unit extent."""
    p = clean_and_create(base / "spatial-pixel-is-point.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    make_array(g, "ar", (9, 9))
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [SPATIAL_CONVENTION, PROJ_CONVENTION],
            "spatial:dimensions": ["y", "x"],
            "spatial:transform": [1.0, 0.0, 0.0, 0.0, -1.0, 8.0],
            "spatial:bbox": [0.0, 0.0, 8.0, 8.0],
            "spatial:registration": "node",
            "proj:code": "EPSG:4326",
        },
    )
    add_consolidated_metadata(p)


def gen_spatial_registration_default(base: Path):
    """Omits spatial:registration - readers must default to pixel."""
    p = clean_and_create(base / "spatial-registration-default.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    make_array(g, "ar", (8, 8))
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [SPATIAL_CONVENTION, PROJ_CONVENTION],
            "spatial:dimensions": ["y", "x"],
            "spatial:transform": [1.0, 0.0, 0.0, 0.0, -1.0, 8.0],
            "spatial:bbox": [0.0, 0.0, 8.0, 8.0],
            "proj:code": "EPSG:4326",
        },
    )
    add_consolidated_metadata(p)


def gen_spatial_sharded(base: Path):
    """Sharded variant of spatial-north-up: sharding_indexed codec."""
    p = clean_and_create(base / "spatial-sharded.zarr")
    store = zarr.storage.LocalStore(str(p))
    g = zarr.open_group(store=store, mode="w", zarr_format=3)
    data = gradient_data((16, 16))
    arr = g.create_array(
        "ar",
        shape=(16, 16),
        dtype="uint8",
        chunks=(8, 8),
        shards=(16, 16),
        fill_value=0,
        dimension_names=["y", "x"],
    )
    arr[:] = data
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [SPATIAL_CONVENTION, PROJ_CONVENTION],
            "spatial:dimensions": ["y", "x"],
            "spatial:transform_type": "affine",
            "spatial:transform": [0.625, 0.0, 0.0, 0.0, -0.625, 10.0],
            "spatial:bbox": [0.0, 0.0, 10.0, 10.0],
            "proj:code": "EPSG:4326",
        },
    )
    add_consolidated_metadata(p)


def gen_spatial_multiband(base: Path):
    """3-band (band, y, x) with spatial:shape distinguishing spatial axes."""
    p = clean_and_create(base / "spatial-multiband.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    data = gradient_data((3, 8, 8), "uint8", band_offset=50)
    make_array(g, "ar", (3, 8, 8), dim_names=("band", "y", "x"), data=data)
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [SPATIAL_CONVENTION, PROJ_CONVENTION],
            "spatial:dimensions": ["y", "x"],
            "spatial:transform": [1.0, 0.0, 0.0, 0.0, -1.0, 8.0],
            "spatial:bbox": [0.0, 0.0, 8.0, 8.0],
            "spatial:shape": [8, 8],
            "proj:code": "EPSG:4326",
        },
    )
    add_consolidated_metadata(p)


# ---------------------------------------------------------------------------
# Valid: multiscale pyramids
# ---------------------------------------------------------------------------


def gen_multiscales_2_levels(base: Path):
    """2-level pyramid, level 1 = 2x block average of level 0."""
    p = clean_and_create(base / "multiscales-2-levels.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    base_data = gradient_data((8, 8), "float32")
    l0 = g.create_group("0")
    make_array(
        l0, "ar", (8, 8), dtype="float32", fill_value=float("nan"), data=base_data
    )
    l1 = g.create_group("1")
    make_array(
        l1,
        "ar",
        (4, 4),
        dtype="float32",
        fill_value=float("nan"),
        data=downsample(base_data, 2).astype("float32"),
    )
    patch_attrs(
        p / "zarr.json",
        {
            "zarr_conventions": [MULTISCALES_CONVENTION],
            "multiscales": {
                "layout": [
                    {
                        "asset": "0",
                        "transform": {"scale": [1.0, 1.0], "translation": [0.0, 0.0]},
                    },
                    {
                        "asset": "1",
                        "derived_from": "0",
                        "transform": {"scale": [2.0, 2.0], "translation": [0.0, 0.0]},
                    },
                ],
                "resampling_method": "average",
            },
        },
    )
    add_consolidated_metadata(p)


def gen_multiscales_sentinel2(base: Path):
    """Sentinel-2 layout (10m/20m/60m), all three conventions composed."""
    p = clean_and_create(base / "multiscales-sentinel2.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    base_data = gradient_data((12, 12), "uint16")
    for name, size, factor in [("r10m", 12, 1), ("r20m", 6, 2), ("r60m", 2, 6)]:
        li = g.create_group(name)
        if factor == 1:
            data = base_data
        else:
            data = downsample(base_data.astype("float64"), factor).astype("uint16")
        make_array(li, "ar", (size, size), dtype="uint16", data=data)
    patch_attrs(
        p / "zarr.json",
        {
            "zarr_conventions": [
                MULTISCALES_CONVENTION,
                PROJ_CONVENTION,
                SPATIAL_CONVENTION,
            ],
            "multiscales": {
                "layout": [
                    {
                        "asset": "r10m",
                        "transform": {"scale": [1.0, 1.0], "translation": [0.0, 0.0]},
                        "spatial:shape": [12, 12],
                        "spatial:transform": [
                            10.0,
                            0.0,
                            500000.0,
                            0.0,
                            -10.0,
                            5000120.0,
                        ],
                    },
                    {
                        "asset": "r20m",
                        "derived_from": "r10m",
                        "transform": {"scale": [2.0, 2.0], "translation": [0.0, 0.0]},
                        "spatial:shape": [6, 6],
                        "spatial:transform": [
                            20.0,
                            0.0,
                            500000.0,
                            0.0,
                            -20.0,
                            5000120.0,
                        ],
                    },
                    {
                        "asset": "r60m",
                        "derived_from": "r10m",
                        "transform": {"scale": [6.0, 6.0], "translation": [0.0, 0.0]},
                        "spatial:shape": [2, 2],
                        "spatial:transform": [
                            60.0,
                            0.0,
                            500000.0,
                            0.0,
                            -60.0,
                            5000120.0,
                        ],
                    },
                ],
                "resampling_method": "average",
            },
            "proj:code": "EPSG:32632",
            "spatial:dimensions": ["y", "x"],
            "spatial:bbox": [500000.0, 5000000.0, 500120.0, 5000120.0],
        },
    )
    add_consolidated_metadata(p)


# ---------------------------------------------------------------------------
# Valid: nodata
# ---------------------------------------------------------------------------


def gen_nodata_float32_nan(base: Path):
    """float32 with NaN fill_value and NaN border rows."""
    p = clean_and_create(base / "nodata-float32-nan.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    data = gradient_data((8, 8), "float32")
    data[0, :] = np.nan
    data[-1, :] = np.nan
    make_array(g, "ar", (8, 8), dtype="float32", fill_value=float("nan"), data=data)
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [SPATIAL_CONVENTION, PROJ_CONVENTION],
            "spatial:dimensions": ["y", "x"],
            "spatial:transform": [1.0, 0.0, 0.0, 0.0, -1.0, 8.0],
            "proj:code": "EPSG:4326",
        },
    )
    add_consolidated_metadata(p)


# ---------------------------------------------------------------------------
# Invalid datasets
# ---------------------------------------------------------------------------

INVALID_DATASETS = {
    "invalid-bad-crs": {
        "violation": "proj: proj:code pattern mismatch",
    },
    "invalid-bad-transform-length": {
        "violation": "spatial: transform must have 6 (2D) or 9 (3D) coefficients",
    },
    "invalid-missing-required": {
        "violation": "spatial: missing required spatial:dimensions",
    },
    "invalid-multiscales-no-transform": {
        "violation": "multiscales: transform required when derived_from present",
    },
    "invalid-multiple-crs": {
        "violation": "proj: multiple CRS fields (oneOf requires exactly one)",
    },
}


def gen_invalid_bad_crs(base: Path):
    """Lowercase epsg:4326 violates pattern ^[A-Z]+:[0-9]+$."""
    p = clean_and_create(base / "invalid-bad-crs.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    make_array(g, "ar", (4, 4))
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [PROJ_CONVENTION],
            "proj:code": "epsg:4326",
        },
    )
    add_consolidated_metadata(p)


def gen_invalid_bad_transform_length(base: Path):
    """spatial:transform with 4 elements instead of required 6."""
    p = clean_and_create(base / "invalid-bad-transform-length.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    make_array(g, "ar", (4, 4))
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [SPATIAL_CONVENTION],
            "spatial:dimensions": ["y", "x"],
            "spatial:transform": [1.0, 0.0, 0.0, -1.0],
        },
    )
    add_consolidated_metadata(p)


def gen_invalid_missing_required(base: Path):
    """spatial: declared but spatial:dimensions missing."""
    p = clean_and_create(base / "invalid-missing-required.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    make_array(g, "ar", (4, 4))
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [SPATIAL_CONVENTION],
            "spatial:transform": [1.0, 0.0, 0.0, 0.0, -1.0, 4.0],
        },
    )
    add_consolidated_metadata(p)


def gen_invalid_multiscales_no_transform(base: Path):
    """derived_from without transform (schema if/then violation)."""
    p = clean_and_create(base / "invalid-multiscales-no-transform.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    l0 = g.create_group("0")
    make_array(l0, "ar", (8, 8))
    l1 = g.create_group("1")
    make_array(l1, "ar", (4, 4))
    patch_attrs(
        p / "zarr.json",
        {
            "zarr_conventions": [MULTISCALES_CONVENTION],
            "multiscales": {
                "layout": [
                    {"asset": "0", "transform": {"scale": [1.0, 1.0]}},
                    {"asset": "1", "derived_from": "0"},
                ]
            },
        },
    )
    add_consolidated_metadata(p)


def gen_invalid_multiple_crs(base: Path):
    """Both proj:code and proj:wkt2 (schema oneOf violation)."""
    p = clean_and_create(base / "invalid-multiple-crs.zarr")
    g = zarr.open_group(str(p), mode="w", zarr_format=3)
    make_array(g, "ar", (4, 4))
    patch_attrs(
        p / "ar" / "zarr.json",
        {
            "zarr_conventions": [PROJ_CONVENTION],
            "proj:code": "EPSG:32610",
            "proj:wkt2": WKT2_UTM10N,
        },
    )
    add_consolidated_metadata(p)


# ---------------------------------------------------------------------------
# Expected values for self-verification
# ---------------------------------------------------------------------------

EXPECTED_VALUES = {
    "crs-epsg-4326": {"crs": "EPSG:4326"},
    "crs-wkt2": {"has_wkt2": True},
    "crs-projjson": {"has_projjson": True},
    "crs-override": {"band1_crs": "EPSG:4326", "band2_crs": "EPSG:32632"},
    "spatial-north-up": {
        "crs": "EPSG:4326",
        "shape": [8, 8],
        "transform": [1.25, 0.0, 0.0, 0.0, -1.25, 10.0],
        "bbox": [0.0, 0.0, 10.0, 10.0],
    },
    "spatial-rotated": {"crs": "EPSG:32632", "shape": [8, 8]},
    "spatial-pixel-is-point": {
        "crs": "EPSG:4326",
        "shape": [9, 9],
        "registration": "node",
    },
    "spatial-registration-default": {
        "crs": "EPSG:4326",
        "shape": [8, 8],
        "registration_absent": True,
    },
    "spatial-sharded": {
        "crs": "EPSG:4326",
        "shape": [16, 16],
        "transform": [0.625, 0.0, 0.0, 0.0, -0.625, 10.0],
        "bbox": [0.0, 0.0, 10.0, 10.0],
        "has_sharding": True,
        "inner_chunk_shape": [8, 8],
    },
    "spatial-multiband": {
        "crs": "EPSG:4326",
        "shape": [3, 8, 8],
        "spatial_shape": [8, 8],
        "bands": 3,
        "band_origins": [0, 50, 100],
    },
    "nodata-float32-nan": {"nodata": "NaN", "dtype": "float32"},
    "multiscales-2-levels": {
        "level_count": 2,
        "level_shapes": {"0": [8, 8], "1": [4, 4]},
    },
    "multiscales-sentinel2": {
        "level_count": 3,
        "level_shapes": {"r10m": [12, 12], "r20m": [6, 6], "r60m": [2, 2]},
        "crs": "EPSG:32632",
    },
}


# ---------------------------------------------------------------------------
# Manifest builder
# ---------------------------------------------------------------------------


def build_manifest(root: Path) -> dict:
    """Walk valid/ and invalid/ to build machine-readable manifest."""
    manifest = {"version": "1.0.0", "zarr_format": 3, "datasets": []}
    for category in ["valid", "invalid"]:
        cat_path = root / category
        if not cat_path.exists():
            continue
        for sub in sorted(cat_path.rglob("*.zarr")):
            if not (sub / "zarr.json").exists():
                continue
            if any(
                p.suffix == ".zarr"
                for p in sub.relative_to(cat_path).parents
                if str(p) != "."
            ):
                continue
            rel = sub.relative_to(root)
            meta = json.loads((sub / "zarr.json").read_text())
            attrs = meta.get("attributes", {})
            conventions = [c.get("name", "") for c in attrs.get("zarr_conventions", [])]

            if not conventions:
                cm = meta.get("consolidated_metadata", {}).get("metadata", {})
                for child_meta in cm.values():
                    ca = child_meta.get("attributes", {})
                    conventions = [
                        c.get("name", "") for c in ca.get("zarr_conventions", [])
                    ]
                    if conventions:
                        break

            if not conventions:
                for child_zj in sub.glob("*/zarr.json"):
                    ca = json.loads(child_zj.read_text()).get("attributes", {})
                    conventions = [
                        c.get("name", "") for c in ca.get("zarr_conventions", [])
                    ]
                    if conventions:
                        break

            entry = {
                "path": str(rel),
                "valid": category == "valid",
                "conventions": conventions,
            }
            ds_name = sub.stem
            if ds_name in INVALID_DATASETS:
                entry["violation"] = INVALID_DATASETS[ds_name]["violation"]
            if ds_name in EXPECTED_VALUES:
                entry["expected"] = EXPECTED_VALUES[ds_name]
            manifest["datasets"].append(entry)
    return manifest


# ---------------------------------------------------------------------------
# Self-verification
# ---------------------------------------------------------------------------


def _find_array_meta(ds_path):
    """Find the first array zarr.json in a store."""
    for child_zj in sorted(ds_path.rglob("zarr.json")):
        if child_zj == ds_path / "zarr.json":
            continue
        meta = json.loads(child_zj.read_text())
        if meta.get("node_type") == "array":
            return meta, child_zj
    root_meta = json.loads((ds_path / "zarr.json").read_text())
    cm = root_meta.get("consolidated_metadata", {}).get("metadata", {})
    for key in sorted(cm):
        if cm[key].get("node_type") == "array":
            return cm[key], None
    return None, None


def _find_band_meta(ds_path, band_name):
    """Find a specific child array's metadata."""
    zj = ds_path / band_name / "zarr.json"
    if zj.exists():
        return json.loads(zj.read_text())
    root_meta = json.loads((ds_path / "zarr.json").read_text())
    cm = root_meta.get("consolidated_metadata", {}).get("metadata", {})
    return cm.get(band_name)


def verify(root: Path):
    """Check generated datasets against EXPECTED_VALUES."""
    print("\nVerifying datasets...")
    errors = []

    for ds_name, expected in EXPECTED_VALUES.items():
        matches = list(root.rglob(f"{ds_name}.zarr"))
        if not matches:
            errors.append(f"{ds_name}: not found")
            continue
        ds_path = matches[0]
        arr_meta, _ = _find_array_meta(ds_path)
        if arr_meta is None:
            errors.append(f"{ds_name}: no array found")
            continue

        attrs = arr_meta.get("attributes", {})
        group_attrs = json.loads((ds_path / "zarr.json").read_text()).get(
            "attributes", {}
        )

        def check(key, actual, exp):
            if actual != exp:
                errors.append(f"{ds_name}: {key} {actual} != {exp}")

        if "shape" in expected:
            check("shape", arr_meta.get("shape"), expected["shape"])
        if "dtype" in expected:
            check("dtype", arr_meta.get("data_type"), expected["dtype"])
        if "crs" in expected:
            crs = attrs.get("proj:code") or group_attrs.get("proj:code")
            check("crs", crs, expected["crs"])
        if "band1_crs" in expected:
            b1 = _find_band_meta(ds_path, "band1")
            b1_crs = (b1 or {}).get("attributes", {}).get(
                "proj:code"
            ) or group_attrs.get("proj:code")
            check("band1_crs", b1_crs, expected["band1_crs"])
        if "band2_crs" in expected:
            b2 = _find_band_meta(ds_path, "band2")
            b2_crs = (b2 or {}).get("attributes", {}).get("proj:code")
            check("band2_crs", b2_crs, expected["band2_crs"])
        if expected.get("has_wkt2") and not attrs.get("proj:wkt2"):
            errors.append(f"{ds_name}: proj:wkt2 not found")
        if expected.get("has_projjson") and not attrs.get("proj:projjson"):
            errors.append(f"{ds_name}: proj:projjson not found")
        if "registration" in expected:
            check(
                "registration",
                attrs.get("spatial:registration"),
                expected["registration"],
            )
        if expected.get("registration_absent"):
            if attrs.get("spatial:registration") is not None:
                errors.append(f"{ds_name}: registration should be absent")
        if "transform" in expected:
            check("transform", attrs.get("spatial:transform"), expected["transform"])
        if "bbox" in expected:
            check("bbox", attrs.get("spatial:bbox"), expected["bbox"])
        if "spatial_shape" in expected:
            check(
                "spatial_shape", attrs.get("spatial:shape"), expected["spatial_shape"]
            )
        if "nodata" in expected:
            fv = arr_meta.get("fill_value")
            exp_nodata = expected["nodata"]
            if exp_nodata == "NaN":
                if fv != "NaN" and not (isinstance(fv, float) and np.isnan(fv)):
                    errors.append(f"{ds_name}: nodata {fv} != NaN")
            elif fv != exp_nodata:
                errors.append(f"{ds_name}: nodata {fv} != {exp_nodata}")
        if "band_origins" in expected:
            store = zarr.open_group(str(ds_path), mode="r")
            data = store["ar"][:]
            for k, exp_val in enumerate(expected["band_origins"]):
                actual_val = int(data[k, 0, 0])
                if actual_val != exp_val:
                    errors.append(f"{ds_name}: band{k}[0,0]={actual_val} != {exp_val}")
        if expected.get("has_sharding"):
            codecs = arr_meta.get("codecs", [])
            sharding = [c for c in codecs if c.get("name") == "sharding_indexed"]
            if not sharding:
                errors.append(f"{ds_name}: sharding_indexed codec not found")
            else:
                inner = sharding[0].get("configuration", {}).get("chunk_shape")
                check("inner_chunk_shape", inner, expected.get("inner_chunk_shape"))
        if "level_count" in expected:
            root_meta = json.loads((ds_path / "zarr.json").read_text())
            layout = (
                root_meta.get("attributes", {}).get("multiscales", {}).get("layout", [])
            )
            check("level_count", len(layout), expected["level_count"])
        if "level_shapes" in expected:
            cm = (
                json.loads((ds_path / "zarr.json").read_text())
                .get("consolidated_metadata", {})
                .get("metadata", {})
            )
            for level_name, exp_shape in expected["level_shapes"].items():
                arr_key = f"{level_name}/ar"
                level_meta = cm.get(arr_key)
                if level_meta is None:
                    errors.append(f"{ds_name}: {arr_key} not in consolidated_metadata")
                else:
                    check(f"{level_name}_shape", level_meta.get("shape"), exp_shape)

    if errors:
        print(f"FAIL: {len(errors)} errors:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"OK: {len(EXPECTED_VALUES)} datasets verified")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    root = ROOT
    print(f"Generating datasets in {root}")

    # Clean old output
    for d in ["valid", "invalid"]:
        p = root / d
        if p.exists():
            shutil.rmtree(p)

    crs = root / "valid" / "crs"
    gen_crs_variants(crs)
    gen_crs_override(crs)
    print("  crs: 4")

    spatial = root / "valid" / "spatial"
    gen_spatial_north_up(spatial)
    gen_spatial_rotated(spatial)
    gen_spatial_pixel_is_point(spatial)
    gen_spatial_registration_default(spatial)
    gen_spatial_sharded(spatial)
    gen_spatial_multiband(spatial)
    print("  spatial: 6")

    ms = root / "valid" / "multiscales"
    gen_multiscales_2_levels(ms)
    gen_multiscales_sentinel2(ms)
    print("  multiscales: 2")

    nodata = root / "valid" / "nodata"
    gen_nodata_float32_nan(nodata)
    print("  nodata: 1")

    invalid = root / "invalid"
    gen_invalid_bad_crs(invalid)
    gen_invalid_bad_transform_length(invalid)
    gen_invalid_missing_required(invalid)
    gen_invalid_multiscales_no_transform(invalid)
    gen_invalid_multiple_crs(invalid)
    print("  invalid: 5")

    manifest = build_manifest(root)
    manifest_path = root / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    total = len(manifest["datasets"])
    valid = sum(1 for d in manifest["datasets"] if d["valid"])
    print(
        f"\nManifest v{manifest['version']}: {total} datasets ({valid} valid, {total - valid} invalid)"
    )

    if "--verify" in sys.argv:
        verify(root)


if __name__ == "__main__":
    main()
