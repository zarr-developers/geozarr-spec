# Advance conventions from Proposal to Candidate maturity

## Summary

Formally advance the three core conventions (geo-proj, spatial, multiscales) from "Proposal" maturity level to "Candidate" status by documenting implementations and ensuring stability commitments.

## Labels

- `geo-proj`
- `spatial`
- `multiscales`
- `governance`

## Milestone

v1-rc

## Background

All three conventions currently list their maturity as "Proposal" in their README files. The Zarr Conventions framework defines maturity levels based primarily on implementation count:

### Maturity Levels (from Zarr Conventions Framework)

| Maturity | Min Impl # | Description | Stability |
|----------|------------|-------------|-----------|
| **Proposal** | 0 | An idea put forward to gather feedback | Not stable - breaking changes almost guaranteed |
| **Pilot** | 1 | Fleshed out with examples, schema, and 1+ implementations | Approaching stability - breaking changes not anticipated but possible |
| **Candidate** | 3 | Multiple implementers using and standing behind it | Mostly stable - breaking changes require new version, minor changes unlikely. Requires code owner. |
| **Stable** | 6 | Highest level. Community commits to review process for any changes. | Completely stable - all changes require new version and review |
| **Deprecated** | N/A | Superseded or did not work out | DO NOT USE |

### Target for v1.0

For GeoZarr v1.0 release, conventions should reach **Candidate** maturity (3+ implementations).

## Acceptance Criteria

### For Each Convention

- [ ] Specification text finalized
- [ ] JSON Schema stable and tested
- [ ] At least 3 independent implementations documented
- [ ] No unresolved blocking issues
- [ ] Code owner designated in README
- [ ] Maturity field updated to "Candidate" in README

### Process Requirements

- [ ] geo-proj advanced to Candidate
- [ ] spatial advanced to Candidate
- [ ] multiscales advanced to Candidate
- [ ] Implementation reports collected and linked

## Checklist: geo-proj

| Requirement | Status | Notes |
|-------------|--------|-------|
| Spec finalized | | |
| Schema stable | | |
| Implementation 1 | | eopf-geozarr |
| Implementation 2 | | geozarr-examples |
| Implementation 3 | | GDAL (planned) / TiTiler / OpenLayers |
| Code owner designated | | |
| Maturity updated | | |

## Checklist: spatial

| Requirement | Status | Notes |
|-------------|--------|-------|
| Spec finalized | | |
| Schema stable | | |
| Implementation 1 | | eopf-geozarr |
| Implementation 2 | | geozarr-examples |
| Implementation 3 | | GDAL (planned) / TiTiler / OpenLayers |
| Code owner designated | | |
| Maturity updated | | |

## Checklist: multiscales

| Requirement | Status | Notes |
|-------------|--------|-------|
| Spec finalized | | |
| Schema stable | | |
| Implementation 1 | | eopf-geozarr |
| Implementation 2 | | geozarr-examples |
| Implementation 3 | | GDAL (planned) / TiTiler / OpenLayers |
| Code owner designated | | |
| Maturity updated | | |

## Known Implementations to Document

| Implementation | Language | geo-proj | spatial | multiscales |
|----------------|----------|----------|---------|-------------|
| eopf-geozarr | Python | Yes | Yes | Yes |
| geozarr-examples | Python | Yes | Yes | Yes |
| GDAL | C++ | Planned | Planned | Planned |
| OpenLayers | JavaScript | Read | Read | Read |
| TiTiler | Python | Read | Read | Read |

## Path to Stable (Post-v1)

After v1.0 release with Candidate maturity, conventions can advance to Stable when:
- 6+ implementations exist
- Community review process is established (planned for 2026 per framework)
- No breaking changes anticipated

## Dependencies

- #003 (Normative language)
- #010 (Reference implementation documented)

## References

- [Zarr Conventions Framework](https://github.com/zarr-conventions/.github/blob/main/profile/README.md)
- [Discussion on V1 of the Zarr Conventions Framework](https://github.com/orgs/zarr-conventions/discussions/24)
