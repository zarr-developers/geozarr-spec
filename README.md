# GeoZarr Specification

GeoZarr defines geospatial conventions for storing multidimensional georeferenced grids using the Zarr format. The work now focuses on concrete and thematic Zarr conventions that address specific community needs. Each convention provides a clear and self-contained extension for a defined topic and supports practical adoption.

A [Zarr convention](https://github.com/zarr-conventions/zarr-conventions-spec) describes how to encode a given domain or structure in Zarr. It specifies required attributes, metadata structures, and rules that enable consistent interpretation by tools and users.

The GeoZarr specification will be produced once a set of mature conventions forms a coherent and recommended suite.

## Contributing

Contribution guidelines are available in the repository’s contributing document: [Contributing Guide](CONTRIBUTING.md)

## Roadmap

The draft roadmap is maintained on the project wiki:
[RoadMap](https://github.com/zarr-developers/geozarr-spec/wiki/First-Release-RoadMap)

## Conventions

The following conventions are developed or supported:

* **Multiscales Convention** – support for pyramidal map overviews and multidimensional multiscale structures.
  Repository: [https://github.com/zarr-conventions/multiscales](https://github.com/zarr-conventions/multiscales)
* **Geospatial Projection Convention** - defines properties that encode datum and coordinate reference system (CRS) information for geospatial data
  Repository: [https://github.com/zarr-conventions/geo-proj](https://github.com/zarr-conventions/geo-proj)
* **Spatial Convention** - describes the relationship between positional indexes and spatial coordinates (e.g., affine transformations). May be developed to support explicit coordinates and GCPs
  Repository: [https://github.com/zarr-conventions/spatial](https://github.com/zarr-conventions/spatial)
  
Additional conventions under consideration include:

* CF in Zarr (repository and structure TBD)
* DGGS in Zarr (see [https://github.com/zarr-conventions/dggs](https://github.com/zarr-conventions/dggs) to participate in development)
* TileMatrixSet (repository and structure TBD)

## Meetings Information

The GeoZarr SWG meets monthly. Agendas and meeting notes are available at:
[https://hackmd.io/@briannapagan/geozarr-spec-swg](https://hackmd.io/@briannapagan/geozarr-spec-swg)

To receive updates and participate, join the Google group:
[https://groups.google.com/u/2/g/geozarr](https://groups.google.com/u/2/g/geozarr)

## Documents and Resources

Specification draft: `geozarr-spec.md`

Background material and conceptual references:

Demonstration Videos ([Youtube channel](https://youtube.com/playlist?list=PLzPGC4s5HQOPdeLoK1MXK6gEa1x2Az8Dn)):
- Project Presentation (at WGISS-53) [GeoZarr Data Store - Context of the ESA GSTP project](https://youtu.be/NYhh66EstnY)
- Project Presentation (at DAP) [Hyperspectral Data Store and Access Project](https://youtu.be/CfmPppVR-o4)
- Demo: [GeoZarr Visual Portrayals and OpenLayers extension](https://youtu.be/IKURmv6CVGU)
- Demo: [GeoZarr Fast Time Series Plotting](https://youtu.be/Nt1URJqW71o)
- Demo: [GeoZarr Compute and plot NDWI index at runtime](https://youtu.be/UP0DjphdZgM)
- Demo: [GeoZarr Catalogue Integration](https://youtu.be/Nlbo3FJH8lo)
- Demo: [GeoZarr Serverless Visualisation and Pixel-Based Access](https://youtu.be/sKlejJcPKqQ)
- Comparison: [GeoZarr vs COG Performances](https://youtu.be/KGC8mLqlsCs)
- Advanced applications: soon

OpenLayers extension prototype: https://github.com/spacebel/geozarr-openlayers

## License

Content is provided under the CC BY 4.0 licence. Attribution is required.
[http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)

GeoZarr was created initially by Spacebel for the European Space Agency under the GSTP programme.

---

If you want, I can generate this in Markdown with links already formatted, or integrate more details on conventions or structure.
