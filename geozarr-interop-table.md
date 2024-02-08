## GeoZarr Store Support (current spec)

| Tool | Can write | Can read local storage | Can read HTTP | Can read S3 | Can read Azure Blob | Can read GCS |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- |
| GDAL | ？ |  |  |  |  |  |
| QGIS| ⚠️ | ⚠️ |  | ✅* |  |  |
| ArcGIS | n/a | ✅ | | ✅ |  | ✅ |
| NetCDF Python | ？ | ✅ |  |  |  |  |
| NCO | ✅ | ✅ |  |  |  |  |
| Panoply | n/a | 🚫 |  |  |  |  |
| Xarray | ✅ |  |  |  |  |  |

## GeoZarr Tool Interoperability (current spec)

|Reader →  Writer ↓| GDAL | QGIS | ArcGIS | NetCDF Python | NCO | Panoply | Xarray |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| GDAL |  |  |  |  |  | n/a |  |
| QGIS |  |  |  |  |  | n/a |  |
| ArcGIS |  |  |  |  |  | n/a |  |
| NetCDF |  |  |  |  |  | n/a |  |
| NCO |  |  |  |  |  | n/a | ✅ |
| Panoply |  |  |  |  |  | n/a |  |
| Xarray | ✅* | ✅ | ✅ | ✅ | ✅ | n/a | ✅ |

## Sample data
netcdf like data (Written with Xarray): http://tinyurl.com/GLDAS-NOAH025-3H

https://beta.source.coop/zarr/geozarr-tests/

https://github.com/zarr-developers/geozarr-spec/issues/36

## Tools

### GDAL (3.8.3) 


### QGIS (3.34.3)
With GDAL (3.8.1) 

Can read from local storage, but can't read the CRS.

Can read from S3, but extremely slowly.

Can write, but with incorrect nodata value and doesn't write multiple variables to a file. 

### ArcGIS (3.2.1) 

### NetCDF Python Library (1.6.2)
Should be able to read from S3, but depends upon configuring the NetCDF C library with [the NCZarr implementation](https://docs.unidata.ucar.edu/nug/current/nczarr_head.html) to read from S3. Attempting to read from S3 triggered this message: `s3 scheme requires that netCDF be configured with –enable-nczarr-s3 option `.

### NCO (5.1.9)
Ticket: https://github.com/zarr-developers/geozarr-spec/issues/40

Should be able to read from S3, but depends upon configuring the NetCDF C library with [the NCZarr implementation](https://docs.unidata.ucar.edu/nug/current/nczarr_head.html) to read from S3. Attempting to read from S3 triggered this message: `s3 scheme requires that netCDF be configured with –enable-nczarr-s3 option `.

### Panoply (5.2.9)

### Xarray (2024.1.1)
Can read and write, but only if using GDAL <3.6 or no GDAL. Does not work with GDAL 3.8.
