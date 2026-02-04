# Create conformance test dataset suite

## Summary

Develop a comprehensive suite of test GeoZarr datasets that can be used for conformance testing, interoperability validation, and as reference examples.

## Labels

- `testing`

## Milestone

v1-rc

## Background

A standardized test dataset suite is essential for:
- Verifying implementation conformance
- Testing tool interoperability
- Providing concrete examples for developers
- Regression testing as spec evolves

## Acceptance Criteria

- [ ] Covers all conformance classes
- [ ] Includes valid and invalid examples
- [ ] Multiple CRS types represented
- [ ] Various data types (uint8, float32, etc.)
- [ ] Different chunking configurations
- [ ] Hosted publicly for download
- [ ] Documented with expected behavior
- [ ] Small file sizes for quick testing

## Dataset Categories

### 1. Minimal Valid Examples

| Dataset | Conventions | Purpose |
|---------|-------------|---------|
| `minimal-core.zarr` | Core only | Bare minimum valid GeoZarr |
| `minimal-geoproj.zarr` | Core + geo-proj | Minimum CRS example |
| `minimal-spatial.zarr` | Core + spatial | Minimum transform example |
| `minimal-multiscales.zarr` | Core + multiscales | Minimum pyramid example |
| `minimal-full.zarr` | All three | Minimum complete example |

### 2. CRS Variations (geo-proj)

| Dataset | CRS Type | Description |
|---------|----------|-------------|
| `crs-epsg-4326.zarr` | EPSG | WGS84 geographic |
| `crs-epsg-32610.zarr` | EPSG | UTM Zone 10N |
| `crs-epsg-3857.zarr` | EPSG | Web Mercator |
| `crs-wkt2.zarr` | WKT2 | Custom CRS via WKT2 |
| `crs-projjson.zarr` | PROJJSON | Full PROJJSON encoding |
| `crs-inherited.zarr` | Mixed | Group + array level CRS |

### 3. Spatial Transform Variations

| Dataset | Transform | Description |
|---------|-----------|-------------|
| `spatial-north-up.zarr` | Affine | Standard north-up orientation |
| `spatial-rotated.zarr` | Affine | Rotated grid |
| `spatial-pixel-is-area.zarr` | Affine | PixelIsArea registration |
| `spatial-pixel-is-point.zarr` | Affine | PixelIsPoint registration |
| `spatial-high-res.zarr` | Affine | Sub-meter resolution |
| `spatial-global.zarr` | Affine | Global extent |

### 4. Multiscale Variations

| Dataset | Levels | Description |
|---------|--------|-------------|
| `multiscales-2-levels.zarr` | 2 | Minimum pyramid |
| `multiscales-5-levels.zarr` | 5 | Typical pyramid depth |
| `multiscales-irregular.zarr` | 3 | Non-power-of-2 scaling |
| `multiscales-sentinel2.zarr` | 3 | 10m/20m/60m native resolutions |

### 5. Data Type Variations

| Dataset | Type | Description |
|---------|------|-------------|
| `dtype-uint8.zarr` | uint8 | Imagery, categorical |
| `dtype-uint16.zarr` | uint16 | Satellite imagery |
| `dtype-float32.zarr` | float32 | Scientific data |
| `dtype-complex64.zarr` | complex64 | SAR data |

### 6. Invalid Examples (for validator testing)

| Dataset | Error | Description |
|---------|-------|-------------|
| `invalid-no-conventions.zarr` | Missing registration | No zarr_conventions array |
| `invalid-bad-crs.zarr` | Invalid CRS | Malformed EPSG code |
| `invalid-bad-transform.zarr` | Invalid transform | Wrong array length |
| `invalid-missing-required.zarr` | Missing property | Required field absent |

## File Structure

```
test-datasets/
├── README.md                    # Overview and usage
├── manifest.json                # Machine-readable dataset list
├── valid/
│   ├── minimal/
│   ├── crs/
│   ├── spatial/
│   ├── multiscales/
│   └── dtypes/
├── invalid/
│   └── ...
└── scripts/
    ├── generate_datasets.py     # Reproducible generation
    └── validate_all.py          # Batch validation
```

## Hosting

- GitHub releases for versioned downloads
- Consider S3/GCS bucket for direct Zarr access
- Mirror on Zenodo for DOI citation

## Dependencies

- geozarr-examples or eopf-geozarr for generation

## Notes

- Keep individual datasets small (<10MB)
- Use reproducible random seeds for generated data
- Include checksums for integrity verification
- Version test suite alongside spec version
