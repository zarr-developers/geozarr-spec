# GeoZarr-spec 0.4

This document aims to provides a geospatial extension to the Zarr specification (v2). Zarr specifies a protocol and format used for storing Zarr arrays, while the present extension defines **conventions** and recommendations for storing **multidimensional georeferenced grid** of geospatial observations (including rasters). 

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

## Status

This specification is an early draft developed in the frame of an European Space Agency (ESA) GSTP. Through the optional General Support Technology Programme (GSTP) ESA, Participating States and Industry work together to convert promising engineering concepts into a broad spectrum of usable products.

[Change Log](https://github.com/christophenoel/geozarr-spec/wiki)

## GeoZarr Classes

GeoZarr is restricted to geospatial data which conforms to the conceptual class of Dataset as defined below.

### GeoZarr DataArray

A GeoZarr DataArray variable is a **Zarr Array** that provides values of a measured or observed **geospatial phenomena** (possibly indirectly computed using processing). For example, it might provide reflectance values of a captured satellite scene, or it may describe average vegetation index (NDVI) values for defined period of times.

GeoZarr DataArray variable MUST include the attribute **\_ARRAY_DIMENSIONS which list the dimension names** (this property was first introduced by xarray library).


```
"_ARRAY_DIMENSIONS": [
        "lat",
        "lon"
    ]
```    
    
### GeoZarr Coordinates

GeoZarr Coordinates variable is a one dimensional **Zarr Array** that **indexes a dimension** of a GeoZarr DataArray (e.g latitude, longitude, time, wavelength).

GeoZarr Coordinates variable MUST include the attribute **\_ARRAY_DIMENSIONS equal to the Zarr array name** (e.g. latitude for the latitude Zarr Array).

### GeoZarr Auxiliary Data

GeoZarr Auxiliary variable is empty, one dimensional or multidimensional **Zarr Array** providing auxiliary information.

GeoZarr Auxiliary variable MUST include the attribute **\_ARRAY_DIMENSIONS set as an empty array**.

### GeoZarr Dataset

GeoZarr Dataset is a root **Zarr Group** which contains a **set of DataArray variables** (observed data), **Coordinates variables**, Auxiliary variables, and optionally children Datasets (located in children Zarr Groups). Dataset MUST contain a **consistent** set of data for which the DataArray variables have aligned dimensions, and share the same coordinates grid using a common spatial projection.

If multiple Array Variables share heterogeneous dimensions or coordinates, a primary homogeneous set of variables MUST be located at root level, and the other sets declared in children datasets.


## GeoZarr Metadata

GeoZarr Arrays and Coordinates Variables MUST include [Climate and Forecast (CF)](http://cfconventions.org/) attributes (in the .attrs object). The variables MUST include at least:

* standard_name for all variables
* grid_mapping (coordinates reference system) for all array variables

### Standard Name

A CF **standard name** is an attribute which identifies the physical quantity of a variable ([table](https://cfconventions.org/Data/cf-standard-names/78/build/cf-standard-name-table.html)). 

The quantity may describe the observed phenomenon for:
* a DataArray variable (for example 'surface_bidirectional_reflectance' for optical sensor data)
* a Coordinate variable
* an Auxiliary variable

The following standard names are recommended to describe coordinates variables for dimensions of DataArrays:
* grid_latitude, grid_longitude (spatial coordinates as degrees)
* projection_x_coordinate, projection_y_coordinates (spatial coordinates as per projection)
* sensor_band_identifier (multisptrectal band identifier)
* radiation_wavelength (hyperspectral wave length)
* altitude
* time

### Coordinate Reference System

The **grid_mapping** CF variable defined by DataArray variable defines  the coordinate reference system (CRS) used for the horizontal spatial coordinate values. The grid_mapping value indicates the Auxliary variable that holds all the CF attribute describing the CRS. 

### Other CF Properties

All other CF conventions are recommended, in particular the attributes below:

* add_offset
* scale_factor
* units (as per [UDUNITS v2](https://www.unidata.ucar.edu/software/udunits/udunits-2.2.28/udunits2.html))

## Multiscales

A GeoZarr Dataset variable might includes multiscales for a set of DataArray variables.  Also known as overviews, multiscales provides download-scaled versions of the original image and represent zoomed out version of the image for fast visualisation purposes. A zoomed out version of the original image thus holds much less detail.

### Multiscales Encoding 

 Multiscales MUST be encoded in children groups.
 
* Multiscale group name is the zoom level (e.g. '0').
* Multiscale group contains all DataArrays generated for this specific zoom level.
* Zoom level  strategy is based on defacto standard level 0 as 256x256 pixels covering the entire world, and scale doubled on each level as per https://wiki.openstreetmap.org/wiki/Zoom_levels. 
* Multiscale chunking is RECOMMENDED to be 256 pixels or 512 pixels for the latittude and longitude dimensions.

### Multiscales Metadata

Each DataArray MUST define the 'multiscales' metadata attribute that provides the multiscales group path :

* Path MUST be the relative path to the Zarr group which holds the DataArray variable 
* Zoom levels MUST be provided from lowest to highest resolutions
* First level path MUST reference to itself or can be omitted.
* If the optional 'crs' attribute is missing, then the downscaled version is assumed to be non-projected (and can be displayed using a "pseudo plate-carree" projection).

```diff
(mandatory items in red, optional items in green)
+{
+  "multiscales": [
-    {
-      "name": "example",
-      "datasets": [
-        {"path": "0", "level": "0", 
+         "crs": "EPSG:3857"},
-        {"path": "1", "level": "1",
-        {"path": "2", "level": "2"},
-        {"path": ".", "level": "3"}
-      ],
+      "type": "gaussian",
-    }
+  ]
+}
```
## Portrayals and Symbology

A GeoZarr Dataset variable might define a set of visual portrayals of the geospatial data and define an adequate symbology. The symbology model is based on a simplified schema based on OGC Symbology Encoding Implementation Specification https://www.ogc.org/standards/symbol.

* Each portrayal defines a name and a symbology
* Attribute 'channel-selection' MUST define either the RGB channels, or the grey channels to be represented.
* Channel values MUST specify the relative path to the data, and optionally include the group(s), array and index (which can use positional and label-based indexing (see: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html).
* If grey channel is specified, the 'color-map' MAY define the mapping of palette-type raster colors or fixed-numeric pixel values to colors.

```diff
(mandatory items in red, optional items in green)
+{
+  "portrayals": [
-    "name": {
-    "symbology": {
-      "channel-selection": {
+        "red":"B4"
+        "green":"data[3]"
+        "blue":"data['420']"
+        "grey":"data[2]"
-      "colorMap": [
-        "color-map-entry": {
-          "color": "#000000",
+          "label": "0"
-          "quantity": "0" },
-        "color-map-entry": {
-          "color": "#d73027",
+          "label": "50"
-          "quantity": "0.5" }
+         ]
+    }    
+  ]    
+}    
```

## Rechunking

GeoZarr DataArrray MUST specify the paths to the rechunked instance of the data. These duplicates of the data enable optimizing queries on specific dimensions to improve performances (e.g. for requesting time series).

The attribute rechunking list the path the the various instances of the data. The corresponding Zarr metadata provides along the rechunked array provides the chunk size and shape.

```diff
(mandatory items in red, optional items in green)
+  "rechunking": [
-    {
-      "path": "rechunk1"
-    },
-    {
-      "path": "rechunk2"
-    }
+  ]
```

## Use Cases

### Multispectral Data

If the optical sensor captures spectral bands for different resolution, it is RECOMMENDED to hold the highest resolution dataset in the root group, and provide the other resolutions in children groups.

The spectral band SHOULD be represented as a dimension (not as an array neither a group). For identifying the band it is RECOMMENDED to either:
* Use the STAC Band common name (see https://github.com/stac-extensions/eo/blob/main/README.md#common-band-names)
* Use the mission specific identifier

### Hyperspectral Data

The wavelength SHOULD be represented as a dimension.

### Time Series

For level 3+ products, time SHOULD be represented as a dimension. 
When the scene temporal instances are not sharing a common coordinate grid , it is RECOMMENDED to project (interpolate) the scenes in a standard geometry.

## License

(CC BY 4.0) : Content in this repository is licensed under a Creative Commons Attribution 4.0 International  license. Licensees may copy, distribute, display, perform and make derivative works and remixes based on it only if they give the author or licensor the credits (attribution). You can find the complete text of this license at http://creativecommons.org/licenses/by/4.0/.

GeoZarr documentation by Christophe Noël from Spacebel, supported by ScanWorld and other contributors.
