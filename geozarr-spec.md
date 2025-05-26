# GeoZarr-spec 0.5

This document aims to provides a geospatial extension to the Zarr specification (v2). Zarr specifies a protocol and format used for storing Zarr arrays, while the present extension defines **conventions** and recommendations for storing **multidimensional georeferenced grid** of geospatial observations (including rasters). 

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

## Status

This specification is an early draft developed in the frame of an European Space Agency (ESA) GSTP. Through the optional General Support Technology Programme (GSTP) ESA, Participating States and Industry work together to convert promising engineering concepts into a broad spectrum of usable products. GeoZarr became an [Open Geospatial Consortium (OGC) Standards Working Group (SWG)](https://www.ogc.org/announcement/ogc-forms-new-geozarr-standards-working-group-to-establish-a-zarr-encoding-for-geospatial-data/) in January 2024. It is still a work in progress.

[See the README](README.md#changelog)

## Goals

- Compatibility: Ensuring easy compatibility with popular mapping and data analysis tools such as GDAL, Xarray, ArcGIS, QGIS, and other visualization tools, enabling seamless integration into existing workflows.
- Dimensions: Supporting multi-dimensional data, such as hyperspectral and altitude information, to address broad geospatial data requirements.
- Data Discovery: Providing metadata for discovering, accessing, and retrieving the data, including composite products made of multiple data arrays.
- Mixing Data: Facilitating the combination of different types of geospatial data, including satellite images, elevation maps, and weather models, to create comprehensive and informative datasets.
- Flexibility: Allowing scientists and researchers to work with heterogeneous data types and projections in their preferred software and programming languages, promoting flexibility and adaptability in geospatial data processing and analysis.

## Design goals
- Leverage existing standards as much as possible.
- Support a light-weight extension mechanism for extending standards without breaking compatibility.

## Structure

Following the two primary design goals, the first release of GeoZarr will include two components:

1. A translation of existing standards, including Climate and Forecast Conventions and the Open Geospatial Consortium GeoTIFF standard for compatibility with the Zarr specification V2 and V3.
2. A registration point for defining which primary convention and version is used by the Zarr store.
3. A lightweight extension point for defining extensions that conform to the primary convention.

## Defining primary geospatial convention

Following the [proposed Zarr extensions ZEP](https://zeps--67.org.readthedocs.build/en/67/draft/ZEP0010.html), GeoZarr's usage and configuration should be registered in the `extensions` field of each group or array. Two primary conventions are options in GeoZarr v0.5, although more will likely be added in the future. The individual primary conventions have been translated from their native file format for conformance with Zarr specifications V2 and V3 in 

For example, the following defines that the primary convention is the Climate and Forecast (CF) Metadata Conventions:
```
{
    "zarr_format": 3,
    "node_type": "array",
    ...,
    "extensions": [
        {
            "name": "geozarr",
            "must_understand": false,
            "configuration": {
                "primary": {
                    "name": CF,
                    "version": "1.13"
                }
            }
        }
    ]
}
```

For example, the following defines that the primary convention is the Open Geospatial Consortium GeoTIFF convention:
```
{
    "zarr_format": 3,
    "node_type": "array",
    ...,
    "extensions": [
        {
            "name": "geozarr",
            "must_understand": false,
            "configuration": {
                "primary": {
                    "name": OGC-GeoTIFF,
                    "version": "1.0"
                }
            }
        }
    ]
}
```

The configuration may define a list of extensions, which may be added in future GeoZarr releases, that are fully compatible with the primary configuration. For example:

```
{
    "zarr_format": 3,
    "node_type": "array",
    ...,
    "extensions": [
        {
            "name": "geozarr",
            "must_understand": false,
            "configuration": {
                "primary": {
                    "name": CF,
                    "version": "1.13",
                }
                "extensions": [
                {
                    "name": multiscales,
                    "version": "1.0",
                }
                ]
            }
        }
    ]
}
```

## License

(CC BY 4.0) : Content in this repository is licensed under a Creative Commons Attribution 4.0 International  license. Licensees may copy, distribute, display, perform and make derivative works and remixes based on it only if they give the author or licensor the credits (attribution). You can find the complete text of this license at http://creativecommons.org/licenses/by/4.0/.

GeoZarr documentation by Christophe Noël from Spacebel, supported by ScanWorld and other contributors, along with participants of the GeoZarr Standards Working Group.
