# Chunking best practices guide

## Summary

Create a best practices guide for chunking strategies in GeoZarr datasets, covering spatial chunking, temporal chunking, and trade-offs for different access patterns.

## Labels

- `docs`

## Milestone

v1-rc

## Background

The charter (Section 3) identifies "Multi-dimensional optimizations (spatial chunking scheme, temporal chunking scheme)" as a potential area of guidance.

While chunking is a Zarr concern (not GeoZarr-specific), geospatial data has common access patterns that benefit from specific chunking strategies. Users frequently ask for guidance.

## Acceptance Criteria

- [ ] Common access patterns documented
- [ ] Recommended chunk sizes for each pattern
- [ ] Trade-offs clearly explained
- [ ] Cloud vs. local storage considerations
- [ ] Compression interaction documented
- [ ] Examples with benchmarks
- [ ] Decision flowchart included

## Proposed Outline

### 1. Introduction

- What is chunking and why it matters
- Zarr chunking basics
- GeoZarr-specific considerations

### 2. Access Patterns

| Pattern | Description | Optimal Chunking |
|---------|-------------|------------------|
| Spatial tile | Read rectangular regions | Square spatial chunks |
| Time series | Read all times for a point | Small spatial, large temporal |
| Full frame | Read entire spatial extent | Large spatial chunks |
| Mixed | Variable access patterns | Balanced compromise |

### 3. Chunk Size Guidelines

#### Spatial Dimensions

```
Target chunk size: 1-10 MB compressed

For visualization (web maps):
  - 256x256 or 512x512 pixels
  - Aligns with web tile sizes

For analysis:
  - 512x512 to 1024x1024 pixels
  - Balance between parallelism and overhead

For cloud storage:
  - Minimum 1MB to reduce request overhead
  - Consider S3 request costs
```

#### Temporal Dimension

```
For time series analysis:
  - Chunk along full time dimension if possible
  - Or use 30-365 time steps per chunk

For spatial analysis at single time:
  - Chunk size of 1 in time dimension
  - Allows efficient single-frame access
```

### 4. Cloud Storage Considerations

| Factor | Recommendation |
|--------|----------------|
| Request latency | Larger chunks (reduce requests) |
| Request cost | Larger chunks (fewer GET operations) |
| Partial reads | Smaller chunks (less waste) |
| Parallelism | More chunks (better distribution) |

**Rule of thumb:** 1-10 MB chunks for cloud, can be smaller for local.

### 5. Compression Interaction

- Chunking affects compression ratio
- Similar values compress better together
- Consider data correlation when chunking

### 6. Multiscales Chunking

- Lower resolution levels can use same chunk size
- Or scale chunk size with resolution
- Trade-off: consistency vs. efficiency

### 7. Anti-Patterns

| Anti-Pattern | Problem |
|--------------|---------|
| Tiny chunks (<100KB) | Excessive requests, metadata overhead |
| Huge chunks (>100MB) | Memory pressure, slow partial reads |
| Misaligned chunks | Poor cache utilization |
| Ignoring access pattern | Suboptimal for actual use |

### 8. Decision Flowchart

```
Start
  │
  ├─ Primary access pattern?
  │   ├─ Spatial tiles → 512x512 spatial, small temporal
  │   ├─ Time series → small spatial, full temporal
  │   └─ Mixed → 256x256 spatial, medium temporal
  │
  ├─ Storage location?
  │   ├─ Cloud → target 1-10 MB
  │   └─ Local → target 100KB-1MB
  │
  └─ Adjust based on benchmarks
```

### 9. Benchmarking Your Choice

```python
# Example benchmarking code
import time
import zarr

def benchmark_access(store, pattern="spatial"):
    if pattern == "spatial":
        # Time reading 10 random tiles
        ...
    elif pattern == "temporal":
        # Time reading time series at 10 points
        ...
```

## Non-Goals

This guide will NOT:
- Define normative chunking requirements
- Create a new convention for chunking metadata
- Cover non-geospatial chunking scenarios

## Dependencies

None (informative document only)

## References

- Zarr chunking documentation
- Pangeo chunking recommendations
- Cloud-Optimized GeoTIFF best practices
- Xarray chunking guide
