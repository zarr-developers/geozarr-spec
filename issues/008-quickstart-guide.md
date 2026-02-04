# Create quickstart guide

## Summary

Develop a beginner-friendly quickstart guide that enables new users to create, read, and validate their first GeoZarr dataset within 15 minutes.

## Labels

- `docs`

## Milestone

v1-rc

## Background

The charter (Section 4.1) lists "GeoZarr developer resources" as an initial deliverable. A quickstart guide is essential for adoption, lowering the barrier to entry for new users.

## Acceptance Criteria

- [ ] Guide works for users with basic Python knowledge
- [ ] Can be completed in under 15 minutes
- [ ] Covers creating a GeoZarr from scratch
- [ ] Covers reading an existing GeoZarr
- [ ] Covers validating GeoZarr compliance
- [ ] Includes copy-paste code examples
- [ ] Tested on clean environment
- [ ] Published in documentation site

## Proposed Outline

### 1. Introduction (2 min read)
- What is GeoZarr?
- When to use GeoZarr vs. GeoTIFF/NetCDF
- Prerequisites (Python 3.9+, pip/uv)

### 2. Installation (1 min)
```bash
pip install geozarr-examples
# or
uv add geozarr-examples
```

### 3. Create Your First GeoZarr (5 min)

```python
import numpy as np
import zarr
from geozarr_examples.helpers import add_geozarr_metadata

# Create sample raster data
data = np.random.rand(256, 256).astype(np.float32)

# Create Zarr store
store = zarr.open("my_first_geozarr.zarr", mode="w")
store.create_dataset("temperature", data=data, chunks=(64, 64))

# Add GeoZarr metadata
add_geozarr_metadata(
    store,
    crs="EPSG:4326",
    bounds=(-180, -90, 180, 90),
    transform=[1.40625, 0, -180, 0, -0.703125, 90]
)
```

### 4. Read a GeoZarr (3 min)

```python
import xarray as xr
import rioxarray

# Open with xarray
ds = xr.open_zarr("my_first_geozarr.zarr")

# Access CRS
print(ds.rio.crs)

# Plot
ds["temperature"].plot()
```

### 5. Validate Your GeoZarr (2 min)

```bash
geozarr-examples validate my_first_geozarr.zarr
```

### 6. Next Steps
- Link to convention composition guide
- Link to migration guide (GeoTIFF → GeoZarr)
- Link to full API documentation

## Code Requirements

All code examples must:
- [ ] Work with Python 3.9+
- [ ] Use only documented public APIs
- [ ] Include expected output in comments
- [ ] Handle errors gracefully
- [ ] Be tested in CI

## Dependencies

- geozarr-examples library must have stable helper APIs

## Notes

- Consider Jupyter notebook version for interactive learning
- Include troubleshooting section for common errors
- Add links to community support (GitHub Discussions, etc.)
