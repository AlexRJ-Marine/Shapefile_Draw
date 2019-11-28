import geopandas as gpd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

print(world.head())
world.plot()
plt.savefig('map.png', bbox_inches='tight')
plt.show()

