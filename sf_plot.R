library(ggplot2)
library(cowplot)
library (rgdal)
library (rgeos)
library(maptools)


x_range = c(0,15)
y_range = c(25,45)

data_df = data.frame(x_range, y_range)
write.csv(data_df, file = "data.csv", sep = ",")
head(data_df)

poly <- readShapePoly("Countries_WGS84/Countries_WGS84.shp")
polygon <- fortify(poly)

map <- ggplot() + 
  geom_polygon(data=polygon, aes(long, lat, group = group)) +
  coord_cartesian(x_range,y_range, expand=FALSE) + 
  theme_void() + 
  theme(legend.position="none")

map_ax <- ggplot() + 
  geom_polygon(data=polygon, aes(long, lat, group = group)) +
  coord_cartesian(xlim=x_range, ylim=y_range, expand=FALSE) + 

save_plot("map.png",map ,base_asp = 1, base_height = 10)

save_plot("map_ax.png",map_ax ,base_asp = 1, base_height = 10)