# Define conformance classes structure

## Summary

Define the formal conformance class structure for GeoZarr, establishing which requirements are core vs. optional, and how conformance is tested and claimed.

## Labels

- `spec`

## Milestone

v1-rc

## Background

The charter (Section 3) explicitly mentions determining "what should be kept as a part of the GeoZarr core requirements, and what aspects of geospatial data should be kept as separate conformance classes."

OGC standards use conformance classes to:
- Define testable requirements
- Allow partial implementation
- Enable clear conformance claims

## Acceptance Criteria

- [ ] Core conformance class defined with minimum requirements
- [ ] Optional conformance classes defined for each convention
- [ ] Requirements are testable and unambiguous
- [ ] Conformance URIs assigned to each class
- [ ] Abstract test suite outlines how to verify conformance
- [ ] Dependencies between conformance classes documented

## Proposed Conformance Classes

### Core (Required)

**Conformance Class: GeoZarr Core**
- URI: `http://www.opengis.net/spec/geozarr/1.0/conf/core`
- Requirements:
  - Valid Zarr v2 or v3 store
  - `zarr_conventions` array in root `.zattrs`
  - At least one GeoZarr convention declared

### Optional Classes

**Conformance Class: Geospatial Projection**
- URI: `http://www.opengis.net/spec/geozarr/1.0/conf/geo-proj`
- Dependency: Core
- Requirements:
  - Valid `proj:` namespace attributes
  - CRS encoded as EPSG, WKT2, or PROJJSON
  - Inheritance rules followed if group-level

**Conformance Class: Spatial Coordinates**
- URI: `http://www.opengis.net/spec/geozarr/1.0/conf/spatial`
- Dependency: Core
- Requirements:
  - Valid `spatial:` namespace attributes
  - Transform type specified (affine, etc.)
  - Dimension order documented

**Conformance Class: Multiscales**
- URI: `http://www.opengis.net/spec/geozarr/1.0/conf/multiscales`
- Dependency: Core
- Requirements:
  - Valid `multiscales` attribute
  - At least 2 resolution levels
  - Valid transformation between levels

**Conformance Class: Full GeoZarr**
- URI: `http://www.opengis.net/spec/geozarr/1.0/conf/full`
- Dependency: geo-proj + spatial
- Requirements:
  - Both CRS and spatial transform defined
  - Consistent between conventions

## Questions to Resolve

1. Should multiscales require spatial convention, or be independent?
2. Should there be separate conformance classes for Zarr v2 vs. v3?
3. How do we handle conformance for convention composition?

## Dependencies

None (this blocks #001)

## References

- OGC 08-131r3 (Abstract Specification Topic 1: Conformance)
- Existing OGC conformance class examples (GeoTIFF, CoverageJSON)
