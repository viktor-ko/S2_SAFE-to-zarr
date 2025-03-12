In this Jupyter Notebook we will __learn how to convert Sentinel-2 images from SAFE container to multidimensional arrays and store them in a new [.zarr data format](https://zarr.dev/)__, optimized for cloud storage and computing.
The Sentinel-SAFE format is a variation of the [Standard Archive Format for Europe (SAFE)](https://user.eumetsat.int/resources/user-guides/sentinel-safe-format-guide). It is a zip-compressed container for storing Sentinel satellite images and their metadata in different spatial resolutions. While it is a well-established standard format for archiving satellite data, it is not optimized for high-performance cloud computing workflows, due to its structure and large data volume.

### Outline
1. Install and import necessary Python packages
2. Download Sentinel-2 imagery in .SAFE Format from Copernicus Data Space
3. Load Sentinel-2 imagery from .SAFE folder
4. Open Sentinel-2 images as data arrays, stack them, and convert to Zarr format
5. Validate the Zarr file
6. Upload Zarr data to cloud storage (optional)

- [Original Sentinel-2 SAFE product](https://download.dataspace.copernicus.eu/odata/v1/Products(4e2b90e7-3387-411b-b866-63a9bde00d5a)/$value")
- [Converted Zarr file](https://github.com/viktor-ko/S2_SAFE-to-zarr/tree/9fbed03750b20909663fb7d461af21005c4db0e2/sentinel2_rgb.zarr)
