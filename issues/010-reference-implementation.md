# Document reference implementation

## Summary

Formally document eopf-geozarr as the reference implementation for GeoZarr conventions, providing implementation notes, conformance claims, and guidance for other implementers.

## Labels

- `docs`

## Milestone

v1-rc

## Background

The charter (Section 4) states that "reference implementations that fully use GeoZarr should be documented at the same time the candidate Standard goes to vote."

eopf-geozarr (v0.8.0) implements all three conventions and can serve as the reference implementation. This needs to be formally documented.

## Acceptance Criteria

- [ ] Reference implementation status declared
- [ ] Conformance claims documented per class
- [ ] Implementation notes for each convention
- [ ] Known limitations documented
- [ ] Test coverage reported
- [ ] API stability commitment
- [ ] Link from main spec to reference impl

## Documentation Structure

### 1. Conformance Statement

```markdown
## eopf-geozarr Conformance Statement

**Version:** 0.8.0
**GeoZarr Version:** 1.0 (draft)

| Conformance Class | Status | Notes |
|-------------------|--------|-------|
| GeoZarr Core | Conformant | |
| geo-proj | Conformant | Supports EPSG, WKT2, PROJJSON |
| spatial | Conformant | Affine transforms only |
| multiscales | Conformant | Power-of-2 downsampling |
```

### 2. Implementation Notes

#### geo-proj Implementation
- How CRS is stored and retrieved
- PROJJSON generation from pyproj
- Inheritance implementation details

#### spatial Implementation
- Affine transform handling via rasterio/Affine
- Dimension ordering conventions
- Grid registration handling

#### multiscales Implementation
- Downsampling algorithm (averaging)
- Level naming convention
- Transformation calculation

### 3. Known Limitations

| Limitation | Impact | Workaround |
|------------|--------|------------|
| Zarr v2 only | No v3 support | Use zarr-python 2.x |
| Affine only | No other transform types | Resample to regular grid |
| 2D spatial only | No 3D transforms | Use separate Z dimension |

### 4. For Implementers

Guidance for others implementing GeoZarr:

- Required dependencies
- Key design decisions and rationale
- Common pitfalls
- Test cases to verify conformance

## Files to Create/Update

- [ ] `data-model/CONFORMANCE.md` - Conformance statement
- [ ] `data-model/docs/implementation-notes.md` - Detailed notes
- [ ] `geozarr-spec/implementations.md` - Registry of implementations

## Implementation Registry

Create a registry of known implementations. Per the [Zarr Conventions Framework](https://github.com/zarr-conventions/.github/blob/main/profile/README.md), reaching **Candidate** maturity requires 3+ implementations, and **Stable** requires 6+.

| Implementation | Language | Maintainer | geo-proj | spatial | multiscales |
|----------------|----------|------------|----------|---------|-------------|
| eopf-geozarr | Python | ESA/Spacebel | Full | Full | Full |
| geozarr-examples | Python | GeoZarr SWG | Full | Full | Full |
| GDAL | C++ | OSGeo | Planned | Planned | Planned |
| OpenLayers | JavaScript | OpenLayers | Read | Read | Read |
| TiTiler | Python | Development Seed | Read | Read | Read |

**Current implementation count:** ~4-5 (depending on read-only counting)
**Target for Candidate:** 3+ ✓
**Target for Stable:** 6+

## Dependencies

- #002 (Conformance classes must be defined)
- #011 (Test suite for conformance verification)

## Notes

- Coordinate with eopf-geozarr maintainers
- Consider creating a conformance badge/logo
- Plan for updating as implementation evolves
