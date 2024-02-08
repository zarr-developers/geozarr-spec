"""Create a GeoTIFF and convert it to a Zarr file with CRS metadata, that gets read by QGIS with GDAL 3.8+."""

# (`conda install qgis; qgis` to get qgis with GDAL 3.8+)."""
# There's an open issue to remove `attrs` in Zarr V3, though GDAL's behaviour currently relies on attrs https://github.com/zarr-developers/zarr-python/issues/1624

import affine
import numpy as np
import rasterio
import rioxarray as rxr


def get_some_test_data(bands: int, height: int, width: int) -> np.ndarray:
    """Create some test data."""
    data = np.zeros((bands, height, width), dtype=np.float32)
    for b in range(bands):
        random_value = np.random.rand()
        data[b] = np.sin(np.linspace(0, np.pi, height)[:, None] * random_value)
    return data


def save_to_geotiff(data: np.ndarray, transform: affine.Affine, filename: str = "some.tif") -> None:
    """Save data to a GeoTIFF file."""
    kwargs = {
        "driver": "GTiff",
        "count": data.shape[0],
        "height": data.shape[1],
        "width": data.shape[2],
        "dtype": rasterio.float32,
        "crs": "EPSG:6933",
        "transform": transform,
        "compress": "DEFLATE",
    }

    with rasterio.open(filename, "w", **kwargs) as dst:
        dst.write(data)


def tif_to_crs_zarr(tif_path: str, zarr_path: str, x: str = "x", y: str = "y") -> None:
    """Convert a GeoTIFF file to a Zarr file with valid CRS metadata."""
    da = rxr.open_rasterio(tif_path)
    name = tif_path.split(".")[0].split("/")[-1]
    ds = da.to_dataset(name=name)
    # get the epsg code from the tif file
    epsg = ds.rio.crs.to_epsg()

    # Once your data goes beyond X, Y and 1 data variable,
    # qgis let's you choose which variable to open, as it inherits gdal behavior:
    # https://gdal.org/drivers/raster/zarr.html#particularities-of-the-classic-raster-api
    ds = ds.drop_vars(["band", "spatial_ref"], errors="ignore")
    # renamed x and y to X and Y for gdal to automatically recognize them as spatial dimensions
    ds = ds.rename({x: "X", y: "Y"})
    # add CRS to the dataset following the gdal implementation
    ds.some.attrs["_CRS"] = {"url": f"http://www.opengis.net/def/crs/EPSG/0/{epsg}"}
    ds.to_zarr(f"{name}.zarr", mode="w", consolidated=True)


if __name__ == "__main__":
    width, height, bands = 8192, 8192, 3
    # create affine transformation
    transform = affine.Affine(10.0, 0.0, 400000.0, 0.0, -10.0, 6000000.0)
    # create some test data
    data = get_some_test_data(bands, height, width)
    tif_filename = "some.tif"
    save_to_geotiff(data, transform, filename=tif_filename)
    # convert tif to zarr
    tif_to_crs_zarr(tif_filename, "some.zarr", x="x", y="y")
