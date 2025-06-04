# GeoZarr-Spec

GeoZarr Spec aims to provide a geospatial extension to the Zarr specification. Zarr specifies a protocol and format used for storing Zarr arrays, while the present extension defines **conventions** and recommendations for storing **multidimensional georeferenced grid** of geospatial observations (including rasters). 

The latest Editor's Draft version of OGC GeoZarr Specifications found here in [HTML](https://zarr.dev/geozarr-spec/documents/standard/template/geozarr-spec.html) or [PDF](https://zarr.dev/geozarr-spec/documents/standard/template/geozarr-spec.pdf)

The following writings aim to introduce the fundamental concepts of geospatial data models and outline the context and motivation underpinning the development of GeoZarr:

- [Structure Of GeoSpatial Data Systems](https://medium.com/@christophe.noel/structure-of-geospatial-data-ystems-4033d672c222?source=your_stories_page)
- [Geospatial Data Storage Model](https://medium.com/@christophe.noel/geospatial-data-storage-model-d7c3fb895031?source=your_stories_page)
- [Geospatial Data Model Encoding](https://medium.com/@christophe.noel/geospatial-data-model-encoding-1699f4cd5fb9?source=your_stories_page)
- [Geospatial Ecosystems — Scientific vs GIS Communities](https://medium.com/@christophe.noel/geospatial-ecosystems-scientific-vs-gis-communities-324b340bee1a?source=your_stories_page)
- [Motivation for a GeoZarr Unified EO Data Model](https://medium.com/@christophe.noel/motivation-for-a-geozarr-unified-eo-data-model-926dd2bec07a?source=your_stories_page)


# Meetings Information
The GeoZarr SWG meets monthly with an agenda and notes kept [here](https://hackmd.io/@briannapagan/geozarr-spec-swg).

To receive updates about meetings and current efforts, join the Google group by navigating to [https://groups.google.com/u/2/g/geozarr](https://groups.google.com/u/2/g/geozarr) and click "Join this group". 

## Status

This specification early drafts (<=v0.4) were created initially by [Spacebel](https://www.spacebel.com/) for the [European Space Agency](https://esa.int) under the [General Support Technology Programme](http://www.esa.int/Enabling_Support/Space_Engineering_Technology/Shaping_the_Future/About_the_General_Support_Technology_Programme_GSTP).

**Update 2023-01-20** - This spec is transitioning to community-based development in anticipation of submission as an OGC standard. It has been moved to the `zarr-developers` GitHub organization. Brianna Pagan ([@briannapagan](https://github.com/briannapagan)) has volunteered to coordinate the community development process.
Feedback from users and implementers will be solicited from the community and incorporated into future drafts.
Information about how to get involved in this process will be announced soon/

## Changelog

### v0.5

* Reformat GeoZarr as a registration of translated, well-supported open standards for Zarr.

### v0.4 

* Added visual portrayals and symbology (instead of quicklook)
* Specified default multiscale non-projection (pseudo 'Plate Carree')

### v0.3

* Refined multiscales metadata (crs and level attributes)

### v0.2

* Specified multiscales zoom level str

## Document and Resources

Specification [Document](geozarr-spec.md)

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

(CC BY 4.0) : Content in this repository is licensed under a Creative Commons Attribution 4.0 International  license. Licensees may copy, distribute, display, perform and make derivative works and remixes based on it only if they give the author or licensor the credits (attribution). You can find the complete text of this license at http://creativecommons.org/licenses/by/4.0/.

GeoZarr was created initially by [Spacebel](https://www.spacebel.com/) for the [European Space Agency](https://esa.int) under the [General Support Technology Programme](http://www.esa.int/Enabling_Support/Space_Engineering_Technology/Shaping_the_Future/About_the_General_Support_Technology_Programme_GSTP).
