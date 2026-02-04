# Define version stability and compatibility policy

## Summary

Establish a formal versioning policy for GeoZarr conventions, defining what constitutes breaking changes, how versions are assigned, and what compatibility guarantees are provided.

## Labels

- `spec`
- `governance`

## Milestone

v1-rc

## Background

Before v1.0 release, users and implementers need clear expectations about:
- How the specification will evolve
- What changes require new versions
- Backward/forward compatibility guarantees
- Deprecation process

## Acceptance Criteria

- [ ] Semantic versioning policy documented
- [ ] Breaking vs. non-breaking changes defined
- [ ] Compatibility matrix approach established
- [ ] Deprecation timeline and process defined
- [ ] Convention UUID stability guaranteed
- [ ] Schema versioning approach documented

## Proposed Policy

### Semantic Versioning

GeoZarr follows Semantic Versioning 2.0.0:

- **MAJOR** (1.0 → 2.0): Breaking changes to required features
- **MINOR** (1.0 → 1.1): New features, backward compatible
- **PATCH** (1.0.0 → 1.0.1): Bug fixes, clarifications only

### Breaking Changes (Require Major Version)

- Removing required properties
- Changing property semantics incompatibly
- Changing JSON Schema in ways that invalidate previously valid data
- Removing conformance classes

### Non-Breaking Changes (Minor Version)

- Adding new optional properties
- Adding new conformance classes
- Extending allowed values (e.g., new transform types)
- Adding new conventions

### Convention UUIDs

- UUIDs are permanent identifiers and MUST NOT change
- UUID identifies the convention, not the version
- Version is tracked separately in `zarr_conventions` metadata

### Deprecation Policy

1. Features deprecated in version N
2. Deprecation warning in version N+1
3. Removal allowed in version N+2 (major)
4. Minimum 12 months between deprecation and removal

### Schema Versioning

- Each schema includes a `$id` with version
- Schemas are immutable once released
- New versions get new `$id` URIs

## Questions to Resolve

1. Should each convention have independent versions, or one unified version?
2. How do we version the composition of conventions?
3. What is the support timeline for older versions?

## Dependencies

None

## Relationship to Convention Maturity

The [Zarr Conventions Framework](https://github.com/zarr-conventions/.github/blob/main/profile/README.md) defines maturity levels that interact with versioning:

| Maturity | Stability Expectation |
|----------|----------------------|
| Proposal | Breaking changes expected |
| Pilot | Breaking changes not anticipated but possible |
| Candidate | Breaking changes require new version |
| Stable | All changes require new version and review process |

Version stability commitments should align with maturity level.

## References

- Semantic Versioning 2.0.0: https://semver.org/
- [Zarr Conventions Framework](https://github.com/zarr-conventions/.github/blob/main/profile/README.md)
- [Discussion on V1 of the Zarr Conventions Framework](https://github.com/orgs/zarr-conventions/discussions/24)
- OGC standard versioning practices
