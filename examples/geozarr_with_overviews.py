"""Create a GeoTIFF, convert to a premature(!) "GeoZarr" with pyramid overviews."""

# This is a toy problem to demonstrate the creation of a GeoTIFF and the conversion to a Zarr store with overviews.

import shutil

import affine
import numpy as np
import pandas as pd
import rasterio
import rioxarray
import xarray as xr


def get_some_test_data(bands, height, width):
    """Create some test data."""
    data = np.zeros((bands, height, width), dtype=np.float32)
    for b in range(bands):
        random_value = np.random.rand()
        data[b] = np.sin(np.linspace(0, np.pi, height)[:, None] * random_value)
    return data


def save_to_geotiff(
    data: np.ndarray, transform: affine.Affine, filename: str = "some.tif", overviews: list[int] = None
) -> None:
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
        overviews = overviews
        dst.build_overviews(overviews, resampling=rasterio.enums.Resampling.average)
        dst.update_tags(ns="rio_overview", resampling="average")


def add_geozarr_metadata(
    da: xr.DataArray, variable_name: str = "reflectance", crs: str = "EPSG:6933", overviews: list[int] = None
):
    """Add GeoZarr-specific metadata and CF conventions to an xarray DataArray.

    Based on https://github.com/zarr-developers/geozarr-spec/blob/b9f4ad3/geozarr-spec.md.

    NEEDS REVIEWS!!

    Args:
        da: xarray DataArray to add metadata to.
        variable_name: Standard name of the variable for CF 'standard_name' attribute.
        crs: Coordinate Reference System in EPSG code.
        overviews: aggregation overviews
    """
    # _ARRAY_DIMENSIONS: Specifies the dimension names in the order they appear.
    da.attrs["_ARRAY_DIMENSIONS"] = list(da.dims)

    # Climate and Forecast (CF) Attributes
    # CF standard name for the physical quantity.
    da.attrs["standard_name"] = variable_name
    # Points to the variable containing CRS info.
    da.attrs["grid_mapping"] = "spatial_ref"

    # Example of adding grid_mapping info directly in the DataArray
    da["spatial_ref"] = xr.DataArray(
        0,
        attrs={
            "grid_mapping_name": "transverse_mercator",
            "epsg_code": crs,
            "semi_major_axis": 6378137,
            "inverse_flattening": 298.257223563,
        },
    )

    # Multiscales Metadata
    # This is a placeholder showing where multiscale metadata could be added.
    da.attrs["multiscales"] = [
        {
            "datasets": [{"path": f"overview_{overview}", "overview": str(overview)} for overview in overviews],
            "type": "overview",
            "version": "1.0",
        }
    ]

    # Additional CF Attributes for enhanced description and interoperability
    # Assuming reflectance is unitless; adjust based on actual variable.
    da.attrs["units"] = "1"
    da.attrs["scale_overview"] = 1.0
    da.attrs["add_offset"] = 0.0

    # Including documentation and descriptive metadata
    da.attrs["long_name"] = f"{variable_name} measured as reflectance"
    da.attrs["comment"] = "Generated for demonstration purposes"

    # Versioning information for tracking dataset updates
    da.attrs["version"] = "1.0.0"
    da.attrs["history"] = f"Created on {pd.Timestamp.now().strftime('%Y-%m-%d')}"


def to_pyramid_zarr(da: xr.DataArray, zarr_file: str, overviews: list[int]):
    """Convert dataarray to coarsened dataset."""
    shutil.rmtree(zarr_file, ignore_errors=True)
    ds = da.to_dataset(name="data")
    add_geozarr_metadata(ds, overviews=overviews)
    ds.to_zarr(zarr_file, mode="w")

    for overview in overviews:
        da_coarsened = da.coarsen(x=overview, y=overview, boundary="trim").mean()
        # Do we need to copy metadata?
        da_coarsened.attrs = da.attrs  # Copy metadata
        add_geozarr_metadata(da_coarsened, overviews=overviews)
        group_path = f"/overview_{overview}"
        # Add coarsened data to the zarr store
        da_coarsened.to_dataset(name="data").to_zarr(zarr_file, mode="a", group=group_path)


if __name__ == "__main__":
    overviews = [2, 4, 8, 16, 32, 64]
    width, height, bands = 8192, 8192, 3
    # create affine transformation
    transform = affine.Affine(10.0, 0.0, 400000.0, 0.0, -10.0, 6000000.0)
    data = get_some_test_data(bands, height, width)
    tif_filename = "some.tif"
    save_to_geotiff(data, transform, filename=tif_filename, overviews=overviews)
    da = rioxarray.open_rasterio(tif_filename, masked=True)
    to_pyramid_zarr(da, "multiscale_zarr", overviews)
