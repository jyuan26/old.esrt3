import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt

PRISM_DIR = '/Users/jasonyuan/ESRT/dataset/PRISM_ppt_stable_4kmD2_20210101_20211231_bil'
date = '20210101'
pathname = PRISM_DIR+'PRISM_ppt_stable_4kmD2_'+date+'_bil.nc'

## Load the daily netcdf file
pr = xr.open_dataset("/Users/jasonyuan/ESRT/dataset/PRISM_ppt_stable_4kmD2_20210101_20211231_bil")
