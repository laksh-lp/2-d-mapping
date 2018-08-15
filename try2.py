import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import math
lati = 13.352256
loni = 74.798603
latf = 13.360000
lonf = 74.800000
lat3 = 13.360000
lon3 = 74.803000
latmin = lati - 0.010000
lonmin = loni - 0.010000
latmax = lati + 0.010000
lonmax = loni + 0.010000


verts1 = [
    (lati, loni), # left, bottom
    (latf, lonf), # left, top
    ]

verts2 = [
    (lati, loni), # left, bottom
    (lat3, lon3), # left, top
    ]

codes = [Path.MOVETO,
         Path.LINETO,
        ]

path1 = Path(verts1, codes)
path2 = Path(verts2, codes)


    


tan1=(lonf-loni)/(latf-lati)
tan2=(lon3-loni)/(lat3-lati)
tan = tan2 -tan1
theta1 = math.atan(tan)
theta1 = (theta1*180)/3.14

print(theta1)
fig = plt.figure()
ax = fig.add_subplot(111)
patch1 = patches.PathPatch(path1, facecolor='orange', lw=2)
patch2 = patches.PathPatch(path2, facecolor='orange', lw=2)
ax.add_patch(patch1)
ax.add_patch(patch2)
ax.set_xlim(latmin,latmax)
ax.set_ylim(lonmin,lonmax)
ax.plot(lati, loni, marker='*', color='red', markersize=10)
ax.plot(latf, lonf, marker='*', color='red', markersize=10)
ax.plot(lat3, lon3, marker='o', color='green', markersize=5)

ax.plot(latmin + 0.002, lonmax - 0.002, marker=(6, 0, -theta1), color='red', markersize=50)

lat = lati
lon = loni
while(lat < latf and lon < lonf):
    lat = lat + 0.0003
    lon = lon + 0.0008
    ax.plot(lat,lon,marker='o',markersize=10, color='brown')
    #lat = lat + 0.001
    #lon = lon + 0.001
    #plt.draw()
    plt.pause(1)


plt.show()