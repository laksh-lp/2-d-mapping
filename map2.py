	
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

from gps3 import gps3
gps_socket = gps3.GPSDSocket()
data_stream = gps3.DataStream()
gps_socket.connect()
gps_socket.watch()

xs=[]
ys=[]

lati = 13.347239 
loni = 74.792188
latf = 13.347317
lonf = 74.792139

verts1 = [
    (lati, loni), # left, bottom
    (latf, lonf), # left, top
    ]

codes = [Path.MOVETO,
         Path.LINETO,
        ]

path1 = Path(verts1, codes)



#plt.axis([13.347082, 74.789050, 13.350082, 74.802050])

latmin = lati - 0.001
lonmin = loni - 0.001
latmax = latf + 0.001
lonmax = lonf + 0.001

fig = plt.figure()
ax = fig.add_subplot(111)
patch1 = patches.PathPatch(path1, facecolor='orange', lw=2)
ax.add_patch(patch1)


plt.axis([latmin, latmax, lonmin, lonmax])


plt.plot(lati,loni,marker='o',markersize=5, color='blue')
plt.plot(latf,lonf,marker='o',markersize=5, color='red')

i=0

for new_data in gps_socket:
    if new_data:
        data_stream.unpack(new_data)

        

        #i++

        lat = data_stream.TPV['lat']
        lon = data_stream.TPV['lon']
        if(type(lat) == type('s')):
        	print("Waiting for GPS values")
        	continue
        print(lat,lon)

        xs.append(lat)
        ys.append(lon)

        print(xs[i]) #i  is the current value
        print(ys[i])

        

        #latitude = float(lat)
        #longitude = float(lon)
        # if(i == 0):
        #     continue
        if(lat - xs[i] > 0.0003 or lon - ys[i] > 0.0003):
            continue

        i=i+1

        plt.plot(lat,lon,marker='o',markersize=3, color='green')
        plt.draw()
        plt.pause(0.001)
plt.show()




