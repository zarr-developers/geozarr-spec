# GeoZarr Specification

GeoZarr defines geospatial conventions for storing multidimensional georeferenced grids using the Zarr format. The work now focuses on concrete and thematic Zarr conventions that address specific community needs. Each convention provides a clear and self-contained extension for a defined topic and supports practical adoption.

A Zarr convention describes how to encode a given domain or structure in Zarr. It specifies required attributes, metadata structures, and rules that enable consistent interpretation by tools and users.

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

Additional conventions under consideration include:

* Affine coordinates
* NetCDF to Zarr mapping
* GeoTIFF to Zarr mapping

## Meetings Information

The GeoZarr SWG meets monthly. Agendas and meeting notes are available at:
[https://hackmd.io/@briannapagan/geozarr-spec-swg](https://hackmd.io/@briannapagan/geozarr-spec-swg)

To receive updates and participate, join the Google group:
[https://groups.google.com/u/2/g/geozarr](https://groups.google.com/u/2/g/geozarr)

## Documents and Resources

Specification draft: `geozarr-spec.md`

Background material and conceptual references:

* Structure of Geospatial Data Systems
* Geospatial Data Storage Model
* Geospatial Data Model Encoding
* Geospatial Ecosystems – Scientific vs GIS Communities
* Motivation for a GeoZarr Unified EO Data Model

Demo videos: [https://youtube.com/playlist?list=PLzPGC4s5HQOPdeLoK1MXK6gEa1x2Az8Dn](https://youtube.com/playlist?list=PLzPGC4s5HQOPdeLoK1MXK6gEa1x2Az8Dn)
OpenLayers extension prototype: [https://github.com/spacebel/geozarr-openlayers](https://github.com/spacebel/geozarr-openlayers)

## License

Content is provided under the CC BY 4.0 licence. Attribution is required.
[http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/)

GeoZarr was created initially by Spacebel for the European Space Agency under the GSTP programme.

---

If you want, I can generate this in Markdown with links already formatted, or integrate more details on conventions or structure.
