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

The **grid_mapping** CF variable defined by DataArray variable defines the coordinate reference system (CRS) used for the horizontal spatial coordinate values. The grid_mapping value indicates the Auxliary variable that holds all the CF attribute describing the CRS. 

### Other CF Properties

All other CF conventions are recommended, in particular the attributes below:

* add_offset
* scale_factor
* units (as per [UDUNITS v2](https://www.unidata.ucar.edu/software/udunits/udunits-2.2.28/udunits2.html))

## Multiscales

A GeoZarr Dataset variable might includes multiscales for a set of DataArray variables.  Also known as "overviews", multiscales provides resampled copies of the original data at a coarser resolution. Multiscales of the original data thus always hold less detail. Common use cases for multiscales are fast rendering for visualization purposes and analyzing data at multiple resolution. 

### Multiscales Encoding 

 Multiscales MUST be encoded in children groups. Data at all scales MUST use the same coordinate reference system and must follow ONE common zoom level strategy. The zoom level strategy is modelled in close alignment to the [OGC Two Dimensional Tile Matrix Set](https://docs.ogc.org/is/17-083r4/17-083r4.html) version 2 and the [Tiled Asset STAC extension](https://github.com/stac-extensions/tiled-assets). Each zoom level is described by a Matrix defining the number, layout, origen and pixel size of included tiles. These tiles MUST correspond to the chunk layout along the `lat` and `lon` dimension of the DataArray within a given group.
 
* Multiscale group name is the zoom level identifier (e.g. '0').
* Multiscale group contains all DataArrays generated for this specific zoom level. 
* Multiscale chunking is RECOMMENDED to be 256 pixels or 512 pixels for the latitude and longitude dimensions.

### Multiscales Metadata

If implemented, each DataArray MUST define the 'multiscales' metadata attribute which includes the following fields:
* `tile_matrix_set`
* `tile_matrix_set_limits` (optional)
* `resampling_method`


#### Tile Matrix Set
Tile Matrix Set can be: 
* the name of a well know tile matrix set. Well known Tile Matrix Sets are listed [here](https://schemas.opengis.net/tms/2.0/json/examples/tilematrixset/).
* the URI of a JSON document describing the Tile Matrix Set following the OGC standard.
* a JSON object describing the Tile Matrix Set following the OGC standard (CamelCase!).

Within the Tile Matrix Set
* the Tile Matrix identifier for each zoom level MUST be the relative path to the Zarr group which holds the DataArray variable 
* zoom levels MUST be provided from lowest to highest resolutions
* the `supportedCRS` attribute of the Tile Matrix Set MUST match the crs information defined under **grid_mapping**.
* the tile layout for each Matrix MUST correspond to the chunk layout along the `lat` and `lon` dimension of the corresponding group.


#### Tile Matrix Set Limits
Tile Matrix Sets may describe a larger spatial extent and more resolutions than used in the given dataset.
In that case, users MAY specify [Tile Matrix Set Limits](https://docs.ogc.org/is/17-083r4/17-083r4.html#toc21) as described in the OGC standard to define the minimum and a maximum limits of the indices for each TileMatrix that contains actual data. However, the notation for tile matrix set does not the JSON encoding as described in the OGC standard but follows the STAC Tile Asset encoding for better readability.

If used, Tile Matrix Set Limits
* MUST list all included zoom levels
* MAY list the min and max rows and columns for each zoom level. If omitted, it is assumed that the entire spatial extent is covered (resulting in higher chunk count of the DataArray).

#### Resampling Method
Resampling Method specifies which resampling method is used for generating multiscales. It MUST be one of the following string values. Resampling method MUST be the same across all zoom levels:
* nearest
* bilinear
* cubic
* cubic_spline
* lanczos
* average
* mode
* gauss
* max
* min
* med
* q1
* q3
* sum
* rms

### Multiscale examples
#### Using Well Known Name reference

```diff
(mandatory items in red, optional items in green)
+{
+  "multiscales":
-       { 
-           "tile_matrix_set": "WebMercatorQuad",
-           "resampling_method": "nearest",
-       }
+}
```
#### Using a URI

```diff
(mandatory items in red, optional items in green)
+{
+  "multiscales":
-       { 
-           "tile_matrix_set": "https://schemas.opengis.net/tms/2.0/json/examples/tilematrixset/WebMercatorQuad.json.json",
-           "resampling_method": "nearest",
-       }
+}
```

#### Using a JSON object

```diff
(mandatory items in red, optional items in green)
+{
+  "multiscales":
-       { 
-           "tile_matrix_set": {
-               "id": "WebMercatorQuad",
-               "title": "Google Maps Compatible for the World",
-               "uri": "http://www.opengis.net/def/tilematrixset/OGC/1.0/WebMercatorQuad",
-               "crs": "http://www.opengis.net/def/crs/EPSG/0/3857",
-               "orderedAxes": [
-                   "X",
-                   "Y"
-               ],
-               "wellKnownScaleSet": "http://www.opengis.net/def/wkss/OGC/1.0/GoogleMapsCompatible",
-               "tileMatrices": [
-               {
-               "id": "0",
-               "scaleDenominator": 559082264.028717,
-               "cellSize": 156543.033928041,
-               "pointOfOrigin": [
-                   -20037508.3427892,
-                   20037508.3427892
-               ],
-               "tileWidth": 256,
-               "tileHeight": 256,
-               "matrixWidth": 1,
-               "matrixHeight": 1
-               },
-               {
-               "id": "1",
-               "scaleDenominator": 279541132.014358,
-               "cellSize": 78271.5169640204,
-               "pointOfOrigin": [
-                   -20037508.3427892,
-                   20037508.3427892
-               ],
-               "tileWidth": 256,
-               "tileHeight": 256,
-               "matrixWidth": 2,
-               "matrixHeight": 2
-               },
-           }
-           "resampling_method": "nearest",
-       }
+}
```
#### Setting limits

```diff
(mandatory items in red, optional items in green)
+{
+  "multiscales":
-       { 
-           "tile_matrix_set": "WebMercatorQuad",
+           "tile_matrix_limits: {
-                "0": {},
-                "1": {
+                    "min_tile_col": 0,
+                    "max_tile_col": 0,
+                    "min_tile_row": 0,
+                    "max_tile_row": 0
-                },
-                "2": {
+                    "min_tile_col": 1,
+                    "max_tile_col": 1,
+                    "min_tile_row": 2,
+                    "max_tile_row": 2
-                }
-        },
-           "resampling_method": "nearest",
-       }
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
