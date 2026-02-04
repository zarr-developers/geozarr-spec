# Linked datasets convention

## Summary

Develop a new convention for encoding relationships between multiple related variables with potentially heterogeneous coordinates, enabling discovery and navigation of linked datasets within a GeoZarr store.

## Labels

- `spec`

## Milestone

post-v1

## Background

The charter (Section 3) identifies "Multiple related variables with heterogeneous coordinates (e.g., children or linked datasets)" as a potential conformance class.

Use cases include:
- Satellite products with different bands at different resolutions
- Derived products linked to source data
- Quality flags associated with measurement arrays
- Time-varying data with different temporal sampling

## Acceptance Criteria

- [ ] Convention design documented
- [ ] JSON Schema created
- [ ] Relationship types defined
- [ ] Discovery mechanism specified
- [ ] At least 2 use cases demonstrated
- [ ] Interaction with existing conventions documented

## Proposed Design

### Namespace

`links:` or `related:`

### Relationship Types

| Type | Description |
|------|-------------|
| `derived_from` | This array was computed from the target |
| `quality_for` | Quality/mask array for target data |
| `same_as` | Different representation of same data |
| `part_of` | This array is a component of target |
| `contains` | Target array is a component of this |

### Example Metadata

```json
{
  "zarr_conventions": [
    "f17cb550-5864-4468-aeb7-f3180cfb622f",
    "<links-convention-uuid>"
  ],
  "links:relationships": [
    {
      "target": "/quality/cloud_mask",
      "type": "quality_for",
      "description": "Cloud mask for this band"
    },
    {
      "target": "/bands/B04",
      "type": "derived_from",
      "description": "NDVI computed from B04 and B08"
    }
  ]
}
```

### Discovery

```json
{
  "links:index": {
    "bands": ["/bands/B02", "/bands/B03", "/bands/B04"],
    "quality": ["/quality/cloud_mask", "/quality/snow_mask"],
    "derived": ["/indices/ndvi", "/indices/ndwi"]
  }
}
```

## Use Cases

### Use Case 1: Sentinel-2 Product

```
product.zarr/
├── .zattrs (links:index pointing to all arrays)
├── bands/
│   ├── B02/.zattrs (10m, links to quality)
│   ├── B05/.zattrs (20m, links to quality)
│   └── B09/.zattrs (60m, links to quality)
├── quality/
│   ├── cloud_mask/.zattrs (links:quality_for all bands)
│   └── scl/.zattrs (scene classification)
└── indices/
    └── ndvi/.zattrs (links:derived_from B04, B08)
```

### Use Case 2: Climate Model Output

```
model.zarr/
├── .zattrs
├── temperature/.zattrs (links to uncertainty)
├── temperature_uncertainty/.zattrs (links:quality_for temperature)
└── precipitation/.zattrs (different time steps)
```

## Questions to Resolve

1. Should links be unidirectional or bidirectional?
2. How to handle links to external stores?
3. Should there be a required index at group level?
4. How does this interact with Zarr v3 hierarchy?

## Dependencies

- Core conventions should be stable first
- May inform or be informed by CF-on-Zarr work

## References

- STAC item/asset relationships
- NetCDF ancillary_variables convention
- HDF5 dimension scales
