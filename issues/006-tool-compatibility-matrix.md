# Document tool compatibility matrix

## Summary

Create and maintain a compatibility matrix documenting which tools support which GeoZarr conventions, at what level of support, and with what limitations.

## Labels

- `docs`
- `interop`

## Milestone

v1-rc

## Background

The charter (Section 3, Objective 1) requires "ensuring easy compatibility with popular mapping and data analysis tools such as GDAL, Xarray, ArcGIS, QGIS."

Users need clear documentation of what tools work with GeoZarr and any limitations they should be aware of.

## Acceptance Criteria

- [ ] Matrix covers all major geospatial tools
- [ ] Support level clearly defined (full, partial, none)
- [ ] Convention-specific support documented
- [ ] Known limitations listed
- [ ] Version information included
- [ ] Matrix published in documentation
- [ ] Process for updating matrix established

## Proposed Matrix Format

### Support Levels

| Level | Description |
|-------|-------------|
| Full | Complete read/write support for all features |
| Read | Read support only |
| Partial | Some features supported, see notes |
| Planned | Support in development |
| None | No current support |

### Tool Matrix

| Tool | Version | geo-proj | spatial | multiscales | Notes |
|------|---------|----------|---------|-------------|-------|
| GDAL | 3.x | Planned | Planned | Planned | Read-only, funded development |
| Xarray | 2024.x | Full | Full | Partial | Via rioxarray |
| rioxarray | 0.x | Full | Full | None | |
| QGIS | 3.x | Planned | Planned | Planned | Plugin in development |
| ArcGIS Pro | 3.x | ? | ? | ? | Needs testing |
| OpenLayers | 9.x | Read | Read | Read | Via ol-zarr |
| TiTiler | 0.x | Read | Read | Read | Visualization |
| eopf-geozarr | 0.8 | Full | Full | Full | Reference impl |
| zarr-python | 2.x | N/A | N/A | N/A | Base format only |

## Tools to Evaluate

### Priority 1 (Charter-mentioned)
- [ ] GDAL
- [ ] Xarray / rioxarray
- [ ] ArcGIS Pro
- [ ] QGIS

### Priority 2 (Known adopters)
- [ ] OpenLayers
- [ ] TiTiler
- [ ] Leaflet (via plugins)

### Priority 3 (Ecosystem)
- [ ] GeoServer
- [ ] MapServer
- [ ] SNAP (ESA)
- [ ] Google Earth Engine
- [ ] Microsoft Planetary Computer

## Testing Protocol

For each tool, document:

1. **Test dataset**: Which GeoZarr test files were used
2. **Operations tested**: Open, read values, read CRS, visualize, write
3. **Convention support**: Which attributes are recognized
4. **Failure modes**: What happens with unsupported features
5. **Workarounds**: Any configuration needed

## Dependencies

- #011 (Test dataset suite needed for consistent testing)

## Maintenance

- Matrix should be reviewed quarterly
- Tool version updates tracked
- Community contributions welcomed via PR
