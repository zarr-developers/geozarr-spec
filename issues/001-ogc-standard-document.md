# Create formal OGC Standard document

## Summary

Create the official OGC GeoZarr Standard document in the required OGC format (Asciidoc/HTML), consolidating the three core conventions (geo-proj, spatial, multiscales) into a single normative specification.

## Labels

- `spec`

## Milestone

v1-rc

## Background

The charter deliverables (Section 4.1) specify "OGC GeoZarr Standard" as an initial deliverable. Currently, each convention has its own README-based specification, but there is no unified OGC-format document suitable for the standards process.

The OGC document format requires:
- Standardized front matter (scope, conformance, normative references)
- Formal structure following OGC template
- Clear conformance class definitions
- Normative language (RFC 2119 keywords)

## Acceptance Criteria

- [ ] Document follows OGC Standard template structure
- [ ] Includes all required OGC front matter sections
- [ ] Consolidates geo-proj, spatial, and multiscales specifications
- [ ] Defines clear conformance classes and requirements
- [ ] Uses RFC 2119 normative language throughout
- [ ] Includes normative references to Zarr v2/v3, PROJJSON, etc.
- [ ] Builds successfully to HTML and PDF
- [ ] Reviewed by at least 2 SWG members

## Proposed Structure

```
1. Scope
2. Conformance
3. Normative References
4. Terms and Definitions
5. Conventions
   5.1 Document Conventions
   5.2 Zarr Conventions Registration
6. GeoZarr Core
   6.1 Overview
   6.2 Convention Composition
7. Geospatial Projection Convention (geo-proj)
   7.1 Overview
   7.2 Requirements Class
   7.3 Properties
   7.4 Inheritance Model
8. Spatial Coordinate Convention (spatial)
   8.1 Overview
   8.2 Requirements Class
   8.3 Properties
   8.4 Affine Transforms
9. Multiscales Convention
   9.1 Overview
   9.2 Requirements Class
   9.3 Properties
   9.4 Resolution Levels
Annex A: Conformance Class Abstract Test Suite
Annex B: JSON Schemas (Normative)
Annex C: Examples (Informative)
```

## Dependencies

- #002 (Conformance classes must be defined first)
- #003 (Normative language review)

## Notes

- Consider using the OGC Metanorma toolchain for document generation
- Reference existing OGC standards (GeoTIFF, netCDF) for formatting examples
- Coordinate with OGC staff on template requirements
- Conventions should reach "Candidate" maturity (3+ implementations) per the [Zarr Conventions Framework](https://github.com/zarr-conventions/.github/blob/main/profile/README.md) before OGC standardization
