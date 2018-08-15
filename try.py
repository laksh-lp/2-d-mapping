import numpy as np
import matplotlib.pyplot as plt
import gps, os, time
session = gps.gps()

#lat = input('input latitude')
#lon = input('input longitude')
lati = 13.347586
loni = 74.792201
plt.plot(lati,loni,marker='o',markersize=3, color='red')

latf = 13.348082
lonf = 74.792050
plt.plot(latf,lonf,marker='o',markersize=3, color='red')


latmin = lati - 0.000100
lonmin = loni - 0.000100
latmax = latf + 0.000100
lonmax = lonf + 0.000100

plt.axis([latmin, latmax, lonmin, lonmax])
#latarr=[13.348422,13.349422,13.349522,13.349822]
#lonarr=[74.791994,74.791895,74.793995,74.794995]
#while(True):

while 1:
    os.system('clear')
        
    lat = session.fix.latitude
    lon = session.fix.longitude

    time.sleep(4)

    plt.plot(lat,lon,marker='o',markersize=3, color='green')

    plt.draw()
    plt.show(block=True)
	
	

	