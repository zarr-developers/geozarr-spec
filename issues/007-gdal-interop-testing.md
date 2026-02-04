# GDAL interoperability test suite

## Summary

Develop a comprehensive test suite validating GeoZarr interoperability with GDAL, ensuring that GeoZarr files can be read correctly and that GDAL-written Zarr files follow GeoZarr conventions.

## Labels

- `testing`
- `interop`

## Milestone

v1-rc

## Background

GDAL is the foundational library for geospatial data access, used by QGIS, ArcGIS, and countless other tools. The January 2026 meeting notes indicate GDAL funding has been approved for read-only Multiscales/GeoproJ support.

Interoperability with GDAL is critical for GeoZarr adoption.

## Acceptance Criteria

- [ ] Test suite covers all three conventions
- [ ] Tests run against GDAL development branch with GeoZarr support
- [ ] Round-trip tests (write with eopf-geozarr, read with GDAL)
- [ ] CRS preservation verified
- [ ] Transform accuracy validated
- [ ] Multiscale navigation tested
- [ ] Edge cases documented
- [ ] CI integration for ongoing validation

## Test Categories

### 1. CRS Reading (geo-proj)

| Test | Description |
|------|-------------|
| `test_read_epsg_code` | GDAL correctly interprets EPSG code |
| `test_read_wkt2` | GDAL correctly parses WKT2 string |
| `test_read_projjson` | GDAL correctly parses PROJJSON |
| `test_crs_inheritance` | Group-level CRS applied to arrays |
| `test_crs_override` | Array-level CRS overrides group |

### 2. Spatial Transform (spatial)

| Test | Description |
|------|-------------|
| `test_affine_transform` | GeoTransform correctly extracted |
| `test_pixel_registration` | PixelIsArea vs PixelIsPoint handled |
| `test_dimension_order` | X/Y dimension mapping correct |
| `test_bounds_calculation` | Extent calculated correctly |

### 3. Multiscales

| Test | Description |
|------|-------------|
| `test_overview_discovery` | GDAL finds all resolution levels |
| `test_overview_selection` | Correct level selected for zoom |
| `test_overview_values` | Pixel values correct at each level |

### 4. Round-Trip

| Test | Description |
|------|-------------|
| `test_roundtrip_geotiff` | GeoTIFF → GeoZarr → GDAL read matches |
| `test_roundtrip_values` | Pixel values preserved exactly |
| `test_roundtrip_nodata` | NoData values handled correctly |

### 5. Edge Cases

| Test | Description |
|------|-------------|
| `test_large_coordinates` | High coordinate values (e.g., UTM) |
| `test_antimeridian` | Data crossing 180° longitude |
| `test_polar_projection` | Polar stereographic CRS |
| `test_custom_crs` | Non-EPSG CRS via WKT2 |

## Test Infrastructure

```
tests/
├── gdal/
│   ├── conftest.py          # GDAL version detection, skip if unavailable
│   ├── test_geo_proj.py     # CRS tests
│   ├── test_spatial.py      # Transform tests
│   ├── test_multiscales.py  # Overview tests
│   ├── test_roundtrip.py    # End-to-end tests
│   └── fixtures/            # Test GeoZarr files
```

## Dependencies

- #011 (Test dataset suite)
- GDAL development branch with GeoZarr support

## Notes

- Coordinate with GDAL developers on expected behavior
- Document any GDAL-specific conventions or limitations
- Consider contributing tests upstream to GDAL
- Track GDAL version requirements in compatibility matrix (#006)
