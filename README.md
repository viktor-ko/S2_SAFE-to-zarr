In this Jupyter Notebook we will __learn how to convert Sentinel-2 images from SAFE container to multidimensional arrays and store them in a new [.zarr data format](https://zarr.dev/)__, optimized for cloud storage.
The Sentinel-SAFE format is a variation of the [Standard Archive Format for Europe (SAFE)](https://user.eumetsat.int/resources/user-guides/sentinel-safe-format-guide). It is a zip-compressed container for storing Sentinel satellite images in different spatial resolutions, and their metadata. While it is a well-established standard format for archiving satellite data, it is not optimized for high-performance cloud computing workflows due to its data structure and large volume.

### Outline
1. Install and import necessary Python packages
2. Download Sentinel-2 imagery in .SAFE Format from Copernicus Data Space
3. Load Sentinel-2 imagery from .SAFE folder
4. Open Sentinel-2 images as data arrays, stack them, and convert to Zarr format
5. Validate the Zarr file](#5.-Validate-the-Zarr-file
6. Upload Zarr data to cloud storage (optional)

