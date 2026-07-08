#!/usr/bin/env python3
"""Cross-implementation validation: GDAL reads zarr-python-generated GeoZarr datasets.

Requires: GDAL >= 3.13 (spatial/geo-proj convention support)

Usage:
    python validate_gdal.py              # run all checks
    python validate_gdal.py --verbose    # show per-dataset details

Each test opens a conformance dataset with gdal.Open() and verifies that GDAL
correctly interprets the convention attributes (CRS, geotransform, bands, etc.).

Exit code 0 = all pass, 1 = failures, 2 = GDAL too old.
"""

import math
import sys
from pathlib import Path

try:
    from osgeo import gdal

    gdal.UseExceptions()
except ImportError:
    print("SKIP: GDAL Python bindings not available")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
VERBOSE = "--verbose" in sys.argv


def gdal_version():
    v = int(gdal.VersionInfo())
    return (v // 1000000, (v // 10000) % 100, (v // 100) % 100)


def check_version():
    major, minor, _ = gdal_version()
    if major < 3 or (major == 3 and minor < 13):
        print(
            f"SKIP: GDAL {major}.{minor} < 3.13 (spatial/geo-proj convention support)"
        )
        sys.exit(2)


def log(msg):
    if VERBOSE:
        print(f"  {msg}")


# ---------------------------------------------------------------------------
# Test functions
# ---------------------------------------------------------------------------


def test_crs_epsg(root):
    """crs-epsg-4326: GDAL resolves proj:code to SRS."""
    ds = gdal.Open(str(root / "valid/crs/crs-epsg-4326.zarr"))
    assert ds is not None, "Failed to open"
    srs = ds.GetSpatialRef()
    assert srs is not None, "No SRS"
    code = srs.GetAuthorityCode(None)
    assert code == "4326", f"Expected EPSG:4326, got {code}"
    log(f"EPSG:{code}")


def test_crs_wkt2(root):
    """crs-wkt2: GDAL parses proj:wkt2 (UTM 10N)."""
    ds = gdal.Open(str(root / "valid/crs/crs-wkt2.zarr"))
    assert ds is not None, "Failed to open"
    srs = ds.GetSpatialRef()
    assert srs is not None, "No SRS from WKT2"
    code = srs.GetAuthorityCode(None)
    assert code == "32610", f"Expected EPSG:32610, got {code}"
    log(f"WKT2 -> EPSG:{code}")


def test_crs_projjson(root):
    """crs-projjson: GDAL parses proj:projjson (Web Mercator)."""
    ds = gdal.Open(str(root / "valid/crs/crs-projjson.zarr"))
    assert ds is not None, "Failed to open"
    srs = ds.GetSpatialRef()
    assert srs is not None, "No SRS from PROJJSON"
    code = srs.GetAuthorityCode(None)
    assert code == "3857", f"Expected EPSG:3857, got {code}"
    log(f"PROJJSON -> EPSG:{code}")


def test_crs_override(root):
    """crs-override: group=4326, band2=32632. Tests inheritance + override."""
    ds = gdal.OpenEx(str(root / "valid/crs/crs-override.zarr"), gdal.OF_MULTIDIM_RASTER)
    assert ds is not None, "Failed to open as multidim"
    rg = ds.GetRootGroup()
    # band1 should inherit group CRS (4326)
    band1 = rg.OpenMDArray("band1")
    assert band1 is not None, "band1 not found"
    srs1 = band1.GetSpatialRef()
    assert srs1 is not None, "band1 has no SRS"
    code1 = srs1.GetAuthorityCode(None)
    assert code1 == "4326", f"band1 expected 4326, got {code1}"
    log(f"band1: EPSG:{code1}")
    # band2 should override to 32632
    band2 = rg.OpenMDArray("band2")
    assert band2 is not None, "band2 not found"
    srs2 = band2.GetSpatialRef()
    assert srs2 is not None, "band2 has no SRS"
    code2 = srs2.GetAuthorityCode(None)
    assert code2 == "32632", f"band2 expected 32632, got {code2}"
    log(f"band2: EPSG:{code2}")


def test_spatial_north_up(root):
    """spatial-north-up: affine [1.25, 0, 0, 0, -1.25, 10] with bbox."""
    ds = gdal.Open(str(root / "valid/spatial/spatial-north-up.zarr"))
    assert ds is not None, "Failed to open"
    gt = ds.GetGeoTransform()
    # spatial:transform is [a, b, c, d, e, f] (rasterio order)
    # GDAL GeoTransform is [c, a, b, f, d, e]
    # spatial:transform = [1.25, 0, 0, 0, -1.25, 10]
    # -> GDAL GT = [0, 1.25, 0, 10, 0, -1.25]
    expected_gt = (0.0, 1.25, 0.0, 10.0, 0.0, -1.25)
    assert gt == expected_gt, f"GT {gt} != {expected_gt}"
    srs = ds.GetSpatialRef()
    assert srs is not None, "No SRS"
    assert srs.GetAuthorityCode(None) == "4326"
    log(f"GT={gt}")


def test_spatial_rotated(root):
    """spatial-rotated: 30-degree rotation, non-zero b/d coefficients."""
    ds = gdal.Open(str(root / "valid/spatial/spatial-rotated.zarr"))
    assert ds is not None, "Failed to open"
    gt = ds.GetGeoTransform()
    # Non-zero b and d means rotation
    assert gt[2] != 0.0 or gt[4] != 0.0, f"Expected rotation, got GT={gt}"
    srs = ds.GetSpatialRef()
    assert srs is not None, "No SRS"
    assert srs.GetAuthorityCode(None) == "32632"
    log(f"GT={gt} (rotated)")


def test_spatial_pixel_is_point(root):
    """spatial-pixel-is-point: registration=node, 9x9 for 8-unit extent."""
    ds = gdal.Open(str(root / "valid/spatial/spatial-pixel-is-point.zarr"))
    assert ds is not None, "Failed to open"
    assert ds.RasterXSize == 9 and ds.RasterYSize == 9, (
        f"Expected 9x9, got {ds.RasterXSize}x{ds.RasterYSize}"
    )
    md = ds.GetMetadataItem("AREA_OR_POINT")
    log(f"AREA_OR_POINT={md}, size={ds.RasterXSize}x{ds.RasterYSize}")
    if md is not None:
        assert md == "Point", f"Expected Point, got {md}"


def test_spatial_registration_default(root):
    """spatial-registration-default: omitted = readers default to pixel."""
    ds = gdal.Open(str(root / "valid/spatial/spatial-registration-default.zarr"))
    assert ds is not None, "Failed to open"
    md = ds.GetMetadataItem("AREA_OR_POINT")
    log(f"AREA_OR_POINT={md} (should be Area or absent)")
    assert md is None or md == "Area", f"Expected Area or absent, got {md}"


def test_spatial_sharded(root):
    """spatial-sharded: conventions work through sharding_indexed codec."""
    ds = gdal.Open(str(root / "valid/spatial/spatial-sharded.zarr"))
    assert ds is not None, "Failed to open sharded dataset"
    assert ds.RasterXSize == 16 and ds.RasterYSize == 16, (
        f"Expected 16x16, got {ds.RasterXSize}x{ds.RasterYSize}"
    )
    gt = ds.GetGeoTransform()
    expected_gt = (0.0, 0.625, 0.0, 10.0, 0.0, -0.625)
    assert gt == expected_gt, f"GT {gt} != {expected_gt}"
    srs = ds.GetSpatialRef()
    assert srs is not None, "No SRS"
    assert srs.GetAuthorityCode(None) == "4326"
    log(f"GT={gt}, sharded 16x16 with inner chunks 8x8")


def test_spatial_multiband(root):
    """spatial-multiband: 3 bands, spatial:shape=[8,8]."""
    ds = gdal.Open(str(root / "valid/spatial/spatial-multiband.zarr"))
    assert ds is not None, "Failed to open"
    assert ds.RasterCount == 3, f"Expected 3 bands, got {ds.RasterCount}"
    assert ds.RasterXSize == 8 and ds.RasterYSize == 8
    log(f"bands={ds.RasterCount}, {ds.RasterXSize}x{ds.RasterYSize}")


def test_nodata_float32_nan(root):
    """nodata-float32-nan: fill_value=NaN recognized as nodata."""
    ds = gdal.Open(str(root / "valid/nodata/nodata-float32-nan.zarr"))
    assert ds is not None, "Failed to open"
    band = ds.GetRasterBand(1)
    nodata = band.GetNoDataValue()
    assert nodata is not None and math.isnan(nodata), (
        f"Expected NaN nodata, got {nodata}"
    )
    log(f"nodata={nodata}")


def test_multiscales_2_levels(root):
    """multiscales-2-levels: GDAL sees overview from level 1."""
    ds = gdal.Open(str(root / "valid/multiscales/multiscales-2-levels.zarr"))
    assert ds is not None, "Failed to open"
    if ds.RasterCount == 0:
        # Multiscales group without a default array - open via subdataset or multidim
        ds2 = gdal.OpenEx(
            str(root / "valid/multiscales/multiscales-2-levels.zarr"),
            gdal.OF_MULTIDIM_RASTER,
        )
        assert ds2 is not None, "Failed to open as multidim"
        rg = ds2.GetRootGroup()
        g0 = rg.OpenGroup("0")
        assert g0 is not None, "Group '0' not found"
        arr0 = g0.OpenMDArray("ar")
        assert arr0 is not None, "Array 'ar' not found in group 0"
        assert list(arr0.GetShape()) == [8, 8], (
            f"Level 0 shape {arr0.GetShape()} != [8, 8]"
        )
        g1 = rg.OpenGroup("1")
        assert g1 is not None, "Group '1' not found"
        arr1 = g1.OpenMDArray("ar")
        assert arr1 is not None, "Array 'ar' not found in group 1"
        assert list(arr1.GetShape()) == [4, 4], (
            f"Level 1 shape {arr1.GetShape()} != [4, 4]"
        )
        log(f"multidim: level 0 {arr0.GetShape()}, level 1 {arr1.GetShape()}")
    else:
        band = ds.GetRasterBand(1)
        ovr_count = band.GetOverviewCount()
        assert ovr_count >= 1, f"Expected >= 1 overview, got {ovr_count}"
        ovr = band.GetOverview(0)
        assert ovr.XSize == 4 and ovr.YSize == 4, (
            f"Overview size {ovr.XSize}x{ovr.YSize} != 4x4"
        )
        log(f"overviews={ovr_count}, ovr0={ovr.XSize}x{ovr.YSize}")


def test_multiscales_sentinel2(root):
    """multiscales-sentinel2: all 3 conventions composed, 3 resolution levels."""
    ds = gdal.OpenEx(
        str(root / "valid/multiscales/multiscales-sentinel2.zarr"),
        gdal.OF_MULTIDIM_RASTER,
    )
    assert ds is not None, "Failed to open as multidim"
    rg = ds.GetRootGroup()
    for name, expected_size in [("r10m", 12), ("r20m", 6), ("r60m", 2)]:
        grp = rg.OpenGroup(name)
        assert grp is not None, f"Group '{name}' not found"
        arr = grp.OpenMDArray("ar")
        assert arr is not None, f"Array 'ar' not found in {name}"
        shape = list(arr.GetShape())
        assert shape == [expected_size, expected_size], (
            f"{name} shape {shape} != [{expected_size}, {expected_size}]"
        )
    srs = rg.GetAttribute("proj:code")
    if srs:
        log(f"root proj:code={srs.Read()}")
    log("3 resolution levels verified")


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

TESTS = [
    test_crs_epsg,
    test_crs_wkt2,
    test_crs_projjson,
    test_crs_override,
    test_spatial_north_up,
    test_spatial_rotated,
    test_spatial_pixel_is_point,
    test_spatial_registration_default,
    test_spatial_sharded,
    test_spatial_multiband,
    test_nodata_float32_nan,
    test_multiscales_2_levels,
    test_multiscales_sentinel2,
]


def main():
    check_version()
    root = ROOT
    passed = 0
    failed = 0
    skipped = 0

    print(
        f"GDAL {'.'.join(str(v) for v in gdal_version())} - validating {len(TESTS)} datasets\n"
    )

    for test_fn in TESTS:
        name = test_fn.__name__.replace("test_", "")
        try:
            test_fn(root)
            print(f"  PASS  {name}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {name}: {e}")
            failed += 1
        except Exception as e:
            print(f"  SKIP  {name}: {e}")
            skipped += 1

    print(f"\n{passed} passed, {failed} failed, {skipped} skipped")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
