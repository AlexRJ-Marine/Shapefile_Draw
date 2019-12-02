library(ggplot2)
theme_set(theme_bw())
library(cowplot)
library(sf)
library(rnaturalearth)
library(rnaturalearthdata)

x_range = c(-5, 5) #c(-88, -78)
y_range = c(50, 60) #c(24.5, 33)

data_df = data.frame(x_range, y_range)
write.csv(data_df, file = "data.csv", sep = ",")
head(data_df)

world <- ne_countries(scale = "medium", returnclass = "sf")
class(world)

map <- ggplot(data = world) +
    geom_sf() +
    coord_sf(xlim = x_range, ylim = y_range , expand = FALSE) +
    theme_void() + 
    theme(legend.position="none")

save_plot("map.png",map ,base_asp = 1, base_height = 10)