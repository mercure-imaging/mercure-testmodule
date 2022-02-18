# mercure-testmodule
Example module demonstrating a simple image-processing algorithm

## Purpose

This module demonstrates how a simple image-processing algorithm can be integrated and deployed with mercure. In this specific case, the module applies a 2D Gaussian filter to the received DICOM series in a slice-by-slice manner. The module has been written in Python and uses the pydicom package for loading/writing the DICOMs, as well as the SciPy package for applying the Gaussian filter. It also shows how parameters can be passed from the mercure user interface to the module (in this case, the strength of the Gaussian filter).

**NOTE:** Purpose of this module is solely to demonstrate how image-processing algorithms can be integrated into mercure. This module should not be used for any practical applications.

## Installation

The module can be installed on a mercure server using the Modules page of the mercure web interface. Enter the following line into the "Docker tag" field. mercure will automatically download and install the module:
```
mercureimaging/mercure-testmodule
```

The following parameters can be set (via the Modules or Rules page):
```
sigma: Filter strength (default: 7) 
series_offset: Offset added to series number (default: 1000)
```

## Modification

To use the module as template for integrating own algorithms, clone the Git repository into your development environment. Edit the Makefile and replace the tag "mercureimaging/mercure-testmodule" with a tag of your choice (use the name of your own organization in place of "mercureimaging", which will allow you to publish the container image on Docker Hub later). Afterwards, you can build the Docker container locally by calling the "make" command, and you can test the container in mercure by installing the module on the Modules page using the changed tag name. Source code modifications need to be done in the file testmodule.py. If you rename this file, make sure to adapt also the file docker-entrypoint.sh, which is the entry function called by mercure. If you use additional Python libraries, add these libraries to the file requirements.txt to ensure that they get installed when building the container image.
