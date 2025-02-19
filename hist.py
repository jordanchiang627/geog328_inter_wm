# flake8: noqa

import geopandas as gpd
import matplotlib.pyplot as plt

waCovid = gpd.read_file("assets/wa-covid-data.geojson")

waCovid["casePer10k"].dropna().plot.hist(bins = 20, edgecolor = 'black')

plt.show()