# GeoZarr-Spec

GeoZarr Spec aims to provide a geospatial extension to the Zarr specification in the form of a _zarr convention_. Zarr specifies a protocol and format used for storing Zarr arrays, while GeoZarr defines **conventions** and recommendations for storing **multidimensional georeferenced grid** of geospatial observations (including rasters). See this draft [Zarr Enhancement Proposal](https://github.com/zarr-developers/zeps/pull/28/files?short_path=53e442a#diff-53e442aa938ca18ba1a94f845f264c5df0e4650f8f6abda856c3cd819f70abca) for further detail of the Zarr Convention process.

## Scope

* Easy compatibility with popular mapping and data analysis tools like GDAL, Xarray, ArcGIS, and QGIS.
* Combining different types of geospatial data, like satellite images, elevation maps, and weather models.
* Creating and displaying geospatial data in web browsers without complex workarounds
* Helping users discover, access, and retrieve the data they need, including subsets or different arrangements of the data
* Supporting advanced geospatial features for more accurate data representation and analysis.
* Allowing scientists and researchers to work with diverse data types and projections in their preferred software and programming languages.

## Deliverable

The geozarr-spec is a community effort to establish conventions for geospatial use cases in the cloud-native ZARR binary carrier. It is built from existing data standards, conventions, and implementation patterns. The outcome of this work will be an implementable set of conventions. Next steps for formalization of a normative version of the conventions will be refined as the work progresses. Some key considerations follow.

* A ZARR Convention according to the draft described in [Zarr Enhancement Proposal 0004](https://github.com/zarr-developers/zeps/pull/28/files?short_path=53e442a#diff-53e442aa938ca18ba1a94f845f264c5df0e4650f8f6abda856c3cd819f70abca). 
* An OGC standard that describes the GeoZarr-spec convention. ([See two track standards process here for requirements of a full vs community standard](https://docs.opengeospatial.org/pol/05-020r27/05-020r27.html#the-two-track-standards-process-characteristics))
* Contribution of any extension that is best housed in the CF-Convention.

## Status

This specification early drafts (<=v0.4) were created initially by [Spacebel](https://www.spacebel.com/) for the [European Space Agency](https://esa.int) under the [General Support Technology Programme](http://www.esa.int/Enabling_Support/Space_Engineering_Technology/Shaping_the_Future/About_the_General_Support_Technology_Programme_GSTP).

**Update 2023-01-20** - This spec is transitioning to community-based development in anticipation of submission as an OGC standard. It has been moved to the `zarr-developers` GitHub organization. Brianna Pagan ([@briannapagan](https://github.com/briannapagan)) has volunteered to coordinate the community development process.
Feedback from users and implementers will be solicited from the community and incorporated into future drafts.
Information about how to get involved in this process will be announced soon/

## Changelog

### v0.4 

* Added visual portrayals and symbology (instead of quicklook)
* Specified default multiscale non-projection (pseudo 'Plate Carree')

### v0.3

* Refined multiscales metadata (crs and level attributes)

### v0.2

* Specified multiscales zoom level str

## Document and Resources

Specification [Document](geozarr-spec.md) - [Change Log](https://github.com/christophenoel/geozarr-spec/wiki)

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
