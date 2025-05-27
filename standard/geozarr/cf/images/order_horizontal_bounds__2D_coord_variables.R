#!/usr/bin/env Rscript
# R version: >= 4.0.0
# r-svglite version: >= 2.0.0
library(svglite)

# define lat and lon
lon = 10:10
lat = 54:54

# sphere with radius and lon-center and lat-center
radius_grid_lower = 6
radius_grid_low = 7
radius_cell = c(7.5, 7.5, 7.5, 8.5)
radius_grid_high = 8
radius_grid_higher = 9
radius_grid_evenhigher = 10
clon =  7.0
clat = 47.1

## angles center
# 56, 65, 74
## angles bnds
# 51.5, 60.5, 69.5, 78.5

angles_cell = c(56, 65, 74, 65)
angles_grid = c(42.5, 51.5, 60.5, 69.5, 78.5, 87.5)
pi = 3.14
# grid lines above grid cells
ulon_grid_lower = radius_grid_lower * cos(angles_grid/180*pi) + clon
ulat_grid_lower = radius_grid_lower * sin(angles_grid/180*pi) + clat
ulon_grid_low = radius_grid_low * cos(angles_grid/180*pi) + clon
ulat_grid_low = radius_grid_low * sin(angles_grid/180*pi) + clat
# grid cell center coordinates
ulon_cell = radius_cell * cos(angles_cell/180*pi) + clon
ulat_cell = radius_cell * sin(angles_cell/180*pi) + clat
# grid lines below grid cells
ulon_grid_high = radius_grid_high * cos(angles_grid/180*pi) + clon
ulat_grid_high = radius_grid_high * sin(angles_grid/180*pi) + clat
ulon_grid_higher = radius_grid_higher * cos(angles_grid/180*pi) + clon
ulat_grid_higher = radius_grid_higher * sin(angles_grid/180*pi) + clat
ulon_grid_evenhigher = radius_grid_evenhigher * cos(angles_grid/180*pi) + clon
ulat_grid_evenhigher = radius_grid_evenhigher * sin(angles_grid/180*pi) + clat
# radial grid lines
rlon_grid = rbind(ulon_grid_lower, ulon_grid_low, ulon_grid_high, ulon_grid_higher, ulon_grid_evenhigher, NA)
rlat_grid = rbind(ulat_grid_lower, ulat_grid_low, ulat_grid_high, ulat_grid_higher, ulat_grid_evenhigher, NA)

lon_bnds = (10:11) - 0.5
lat_bnds = (54:55) - 0.5

dlon_solid = 0.4
dlat_solid = 0.4
dlon_dot = 1.4
dlat_dot = 0.6
dlon_text1 = 0.1
dlat_text1 = 0.08
dlon_max = 1.8
dlat_max = 0.8

nlon = length(lon)
nlat = length(lat)

# colors
col_grid_draw = '#38598CFF'
col_grid_text = '#440154FF'
col_cell_draw = '#8AD647FF'
col_cell_text = '#8AD647FF'

## write plot to file
# PNG: png('../pics/order_horizontal_bounds__2D_coord_variables.png', width = 7, height = 5.2, units='in', res = 300)
# PDF: pdf('order_horizontal_bounds__2D_coord_variables.pdf', width = 7, height = 5.2, paper='special')
svglite('order_horizontal_bounds__2D_coord_variables.svg', width = 7, height = 5.2)

par(mar = c(4.5, 4.5, 1, 1))

# create base plot
plot(c(ulon_cell[2]), c(ulat_cell[2]),
     xlab = ' ', ylab = '',
     xlim = c(lon_bnds[1] - dlon_dot, lon_bnds[nlon+1] + dlon_max),
     ylim = c(lat_bnds[1] - dlat_dot, lat_bnds[nlat+1] + dlat_max),
     xaxt = 'n', yaxt = 'n',
     bty = 'n', type = 'n')
axis(1, at = c(0, 360))
axis(2, at = c(0, 360))
mtext('longitude', 1, line = +1.2, cex = 2)
mtext('-->  increasing  -->', 1, line = +3, cex = 1.3)
mtext('latitude', 2, line = 2.5, cex = 2)
mtext('-->  increasing  -->', 2, line = 0.8, cex = 1.3)

# add grid ----
# grid lines, solid
lines(ulon_grid_low, ulat_grid_low, col = col_grid_draw, lwd = 2, lty = 'dotted')
lines(ulon_grid_high, ulat_grid_high, col = col_grid_draw, lwd = 2, lty = 'dotted')
lines(ulon_grid_higher, ulat_grid_higher, col = col_grid_draw, lwd = 2, lty = 'dotted')
lines(rlon_grid, rlat_grid, col = col_grid_draw, lwd = 2, lty = 'dotted')

# grid lines, solid
lines(ulon_grid_low[3:4], ulat_grid_low[3:4], col = col_grid_draw, lwd = 2)
lines(ulon_grid_high[3:4], ulat_grid_high[3:4], col = col_grid_draw, lwd = 2)
lines(rlon_grid[c(2:3,6),3:4], rlat_grid[c(2:3,6),3:4], col = col_grid_draw, lwd = 2)

# lines through grid intersection points
# lines(c(ulon_grid_low[4], ulon_grid_low[4]), c(ulat_grid_low[4] - dlat_text1, ulat_grid_low[4] + dlat_text1), col = col_grid_draw)
# lines(c(ulon_grid_low[4] - dlon_text1, ulon_grid_low[4] + dlon_text1), c(ulat_grid_low[4], ulat_grid_low[4]), col = col_grid_draw)
lines(rbind(ulon_grid_low[3:4], ulon_grid_low[3:4], NA), rbind(ulat_grid_low[3:4] - dlat_text1, ulat_grid_low[3:4] + dlat_text1, NA), col = col_grid_draw)
lines(rbind(ulon_grid_low[3:4] - dlon_text1, ulon_grid_low[3:4] + dlon_text1, NA), rbind(ulat_grid_low[3:4], ulat_grid_low[3:4], NA), col = col_grid_draw)
lines(rbind(ulon_grid_high[3:4], ulon_grid_high[3:4], NA), rbind(ulat_grid_high[3:4] - dlat_text1, ulat_grid_high[3:4] + dlat_text1, NA), col = col_grid_draw)
lines(rbind(ulon_grid_high[3:4] - dlon_text1, ulon_grid_high[3:4] + dlon_text1, NA), rbind(ulat_grid_high[3:4], ulat_grid_high[3:4], NA), col = col_grid_draw)

# dots on grid intersection
points(ulon_grid_low[3:4], ulat_grid_low[3:4], pch = 18, cex = 2, col = col_grid_draw)
points(ulon_grid_high[3:4], ulat_grid_high[3:4], pch = 18, cex = 2, col = col_grid_draw)

# lines through grid cell center
lines(c(ulon_cell[2], ulon_cell[2]), c(ulat_cell[2] - dlat_text1, ulat_cell[2] + dlat_text1), col = col_cell_draw)
lines(c(ulon_cell[2] - dlon_text1, ulon_cell[2] + dlon_text1), c(ulat_cell[2], ulat_cell[2]), col = col_cell_draw)
lines(c(ulon_cell[1], ulon_cell[1]), c(ulat_cell[1] - dlat_text1, ulat_cell[1] + dlat_text1), col = col_cell_draw)
lines(c(ulon_cell[1] - dlon_text1, ulon_cell[1] + dlon_text1), c(ulat_cell[1], ulat_cell[1]), col = col_cell_draw)
lines(c(ulon_cell[4], ulon_cell[4]), c(ulat_cell[4] - dlat_text1, ulat_cell[4] + dlat_text1), col = col_cell_draw)
lines(c(ulon_cell[4] - dlon_text1, ulon_cell[4] + dlon_text1), c(ulat_cell[4], ulat_cell[4]), col = col_cell_draw)

# dots in the grid cell center
points(ulon_cell[-3], ulat_cell[-3], pch = 18, cex = 2, col = col_cell_draw)

# add text ----
# bnds
text(ulon_grid_low[4], ulat_grid_low[4] - dlat_text1, 'lonbnd(j,i,0)', col = col_grid_text, cex = 1.5, pos = 1)
text(ulon_grid_low[4] - dlon_text1, ulat_grid_low[4], 'latbnd(j,i,0)', col = col_grid_text, cex = 1.5, pos = 2)
text(ulon_grid_low[3], ulat_grid_low[3] - dlat_text1, 'lonbnd(j,i,1)', col = col_grid_text, cex = 1.5, pos = 1)
# text(ulon_grid_low[3] - dlon_text1, ulat_grid_low[3], 'latbnd(j,i,1)', col = col_grid_text, cex = 1.5, pos = 2)
text(ulon_grid_high[3], ulat_grid_high[3] + dlat_text1, 'lonbnd(j,i,2)', col = col_grid_text, cex = 1.5, pos = 3)
text(ulon_grid_high[3] + dlon_text1, ulat_grid_high[3], 'latbnd(j,i,2)', col = col_grid_text, cex = 1.5, pos = 4)
text(ulon_grid_high[4], ulat_grid_high[4] + dlat_text1, 'lonbnd(j,i,3)', col = col_grid_text, cex = 1.5, pos = 3)
text(ulon_grid_high[4] - dlon_text1, ulat_grid_high[4], 'latbnd(j,i,3)', col = col_grid_text, cex = 1.5, pos = 2)

# grid cell center
text(ulon_cell[2], ulat_cell[2] - dlat_text1, 'lon(j,i)', col = col_cell_text, cex = 1.5, pos = 1)
text(ulon_cell[2] + dlon_text1, ulat_cell[2], 'lat(j,i)', col = col_cell_text, cex = 1.5, pos = 4)
text(ulon_cell[1], ulat_cell[1] - dlat_text1, 'lon(j,i+1)', col = col_cell_text, cex = 1.5, pos = 1)
text(ulon_cell[1] + dlon_text1, ulat_cell[1], 'lat(j,i+1)', col = col_cell_text, cex = 1.5, pos = 4)
text(ulon_cell[4], ulat_cell[4] - dlat_text1, 'lon(j+1,i)', col = col_cell_text, cex = 1.5, pos = 1)
text(ulon_cell[4] + dlon_text1, ulat_cell[4], 'lat(j+1,i)', col = col_cell_text, cex = 1.5, pos = 4)

# close picture output device
dev.off()
