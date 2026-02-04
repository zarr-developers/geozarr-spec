# Add normative language to specifications

## Summary

Review and update all convention specifications to use RFC 2119 normative language (MUST, SHOULD, MAY, etc.) consistently, replacing informal language with precise requirements.

## Labels

- `spec`
- `geo-proj`
- `spatial`
- `multiscales`

## Milestone

v1-rc

## Background

OGC standards require the use of RFC 2119 keywords to clearly distinguish mandatory requirements from recommendations and optional features. The current convention READMEs use informal language that can be ambiguous.

### RFC 2119 Keywords

| Keyword | Meaning |
|---------|---------|
| MUST / REQUIRED / SHALL | Absolute requirement |
| MUST NOT / SHALL NOT | Absolute prohibition |
| SHOULD / RECOMMENDED | May be ignored with good reason |
| SHOULD NOT / NOT RECOMMENDED | May be done with good reason |
| MAY / OPTIONAL | Truly optional |

## Acceptance Criteria

- [ ] RFC 2119 reference added to each specification
- [ ] All requirements use appropriate normative keywords
- [ ] Keywords are consistently capitalized and formatted
- [ ] Ambiguous language identified and clarified
- [ ] Each MUST/SHOULD/MAY is testable
- [ ] Review completed for all three conventions

## Examples of Changes Needed

### geo-proj/README.md

**Before:**
> "The proj:crs property should contain a valid CRS identifier"

**After:**
> "The `proj:crs` property MUST contain a valid CRS identifier when the `proj:` convention is declared."

### spatial/README.md

**Before:**
> "If using an affine transform, the coefficients are provided as an array"

**After:**
> "When `spatial:transform_type` is `affine`, the `spatial:transform` property MUST be an array of exactly 6 numeric values."

### multiscales/README.md

**Before:**
> "Each level in the pyramid can have its own transformation"

**After:**
> "Each level in the `datasets` array MAY include a `coordinateTransformations` property specifying the transformation from the base level."

## Review Checklist

For each convention, review:

- [ ] Property requirements (required vs. optional)
- [ ] Value constraints (types, ranges, formats)
- [ ] Inheritance behavior
- [ ] Error handling / invalid state behavior
- [ ] Interoperability requirements

## Dependencies

- Should be completed before #001 (OGC Standard document)

## References

- RFC 2119: https://www.ietf.org/rfc/rfc2119.txt
- OGC style guide for normative language
