# GeoZarr Conformance Test Datasets

18 Zarr v3 stores (13 valid, 5 invalid) for testing against the v1 convention schemas:
[proj:](https://github.com/zarr-conventions/geo-proj/blob/v1/README.md) |
[spatial:](https://github.com/zarr-conventions/spatial/blob/v1/README.md) |
[multiscales](https://github.com/zarr-conventions/multiscales/blob/v1/README.md)

> **Note**: `proj:` CMO URLs use `zarr-experimental` to match upstream [geo-proj schema.json](https://github.com/zarr-conventions/geo-proj/blob/v1/schema.json) `const` values. Will update when [#126](https://github.com/zarr-developers/geozarr-spec/issues/126) resolves.

```bash
python scripts/generate_datasets.py --verify   # generate + self-check
python scripts/validate_schema.py              # validate against upstream JSON schemas
python scripts/validate_gdal.py                # cross-check with GDAL >= 3.13
```

Requires: `zarr>=3.0`, `numpy`. Schema validation requires `jsonschema`. GDAL validation requires GDAL >= 3.13.

## Datasets

| Dataset | What to check |
|---|---|
| `crs-epsg-4326` | Resolve `proj:code` EPSG code to CRS |
| `crs-wkt2` | Parse `proj:wkt2` string (UTM 10N) |
| `crs-projjson` | Parse `proj:projjson` object (Web Mercator) |
| `crs-override` | Group=4326, band2=32632 - array-level overrides group |
| `spatial-north-up` | Affine `[1.25, 0, 0, 0, -1.25, 10]` with bbox |
| `spatial-rotated` | 30-degree rotation in UTM, omits `transform_type` and `bbox` (both optional) |
| `spatial-pixel-is-point` | `registration: "node"` - 9x9 for 8-unit extent (N+1 pixels) |
| `spatial-registration-default` | Field omitted - readers must default to `"pixel"` |
| `spatial-sharded` | Sharding codec (`sharding_indexed`) - conventions work through sharded storage |
| `spatial-multiband` | Shape (3,8,8), `spatial:shape`=[8,8] identifies spatial axes |
| `multiscales-2-levels` | Level 1 = 2x block-average of level 0 (verifiable) |
| `multiscales-sentinel2` | All conventions composed - 10m/20m/60m Sentinel-2 layout |
| `nodata-float32-nan` | `fill_value: NaN` with actual NaN in border rows |
| **`invalid-bad-crs`** | **`epsg:4326` fails `^[A-Z]+:[0-9]+$` - reject** |
| **`invalid-bad-transform-length`** | **`spatial:transform` with 4 elements (needs 6) - reject** |
| **`invalid-missing-required`** | **`spatial:dimensions` missing - reject** |
| **`invalid-multiscales-no-transform`** | **`derived_from` without `transform` - reject** |
| **`invalid-multiple-crs`** | **Both `proj:code` and `proj:wkt2` (oneOf) - reject** |

Transform order is rasterio/Affine `[a, b, c, d, e, f]`, **not** GDAL GeoTransform.

## For implementers

**Start here**: `crs-epsg-4326` + `spatial-north-up` - the required fields for the most common case.

**Full conformance**: 13 valid pass without error, 5 invalid rejected with diagnostics.

[`manifest.json`](manifest.json) has expected values per dataset for CI. All scripts use exit codes: 0 = pass, 1 = fail, 2 = skip (missing dependency).

Binary Zarr chunks are committed so `git clone` gives working datasets without running Python. To regenerate: `python scripts/generate_datasets.py --verify`.
