# Convention composition guide

## Summary

Create a comprehensive guide explaining how to combine GeoZarr conventions (geo-proj, spatial, multiscales) together, including inheritance rules, common patterns, and best practices.

## Labels

- `docs`
- `geo-proj`
- `spatial`
- `multiscales`

## Milestone

v1-rc

## Background

GeoZarr conventions are designed to be "composable" - they can be used independently or together. However, the interaction between conventions (especially inheritance and override behavior) can be confusing. Users need clear guidance on:

- Which conventions to use for their use case
- How conventions interact when combined
- Common patterns and anti-patterns

## Acceptance Criteria

- [ ] Explains when to use each convention
- [ ] Documents inheritance behavior
- [ ] Shows valid composition patterns
- [ ] Warns about invalid/problematic combinations
- [ ] Includes complete working examples
- [ ] Covers both simple and advanced scenarios
- [ ] Diagrams for visual learners

## Proposed Outline

### 1. Introduction
- Philosophy of composable conventions
- The `zarr_conventions` registration array

### 2. Convention Overview

| Convention | Use When |
|------------|----------|
| geo-proj | You need to specify a coordinate reference system |
| spatial | You need to map array indices to coordinates |
| multiscales | You have multiple resolution levels |

### 3. Common Composition Patterns

#### Pattern A: Simple Georeferenced Raster
- geo-proj + spatial
- Single CRS, single resolution
- Example: Converted GeoTIFF

#### Pattern B: Multi-Resolution Pyramid
- geo-proj + spatial + multiscales
- COG-style overviews
- Example: Web map tiles

#### Pattern C: Multi-CRS Dataset
- geo-proj (at array level, not group)
- Different projections per variable
- Example: Global + regional views

#### Pattern D: Inherited Metadata
- geo-proj at group level
- spatial at array level
- Shared CRS, per-array transforms

### 4. Inheritance Rules

```
Group Level (.zattrs)
├── proj:crs = "EPSG:4326"     ← Inherited by all arrays
├── proj:wkt2 = "..."
│
├── array1/.zattrs
│   └── spatial:transform = [...] ← Uses inherited CRS
│
└── array2/.zattrs
    ├── proj:crs = "EPSG:32610"   ← Overrides group CRS
    └── spatial:transform = [...]
```

### 5. Validation

How to validate that composed conventions are consistent:
- CRS matches between geo-proj and spatial bounds
- Multiscale transforms are mathematically consistent
- No conflicting declarations

### 6. Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| CRS at array, transform at group | Inconsistent inheritance | Keep related metadata together |
| Multiscales without spatial | Can't compute bounds | Add spatial to base level |
| Duplicate convention UUIDs | Invalid registration | Each UUID appears once |

### 7. Complete Examples

- Example 1: Sentinel-2 L2A product (real-world complexity)
- Example 2: Climate model output (time dimension)
- Example 3: DEM with hillshade (derived products)

## Diagrams Needed

- [ ] Convention relationship diagram
- [ ] Inheritance flow diagram
- [ ] Decision tree: "Which conventions do I need?"

## Dependencies

- All three convention specs finalized (#003)

## Notes

- Include JSON snippets that can be copy-pasted
- Reference examples in convention directories
- Consider interactive diagram (Mermaid or similar)
