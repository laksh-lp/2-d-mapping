from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
m= Basemap(projection='mill',
	llcrnrlat = 5.8802,
	llcrnrlon = 63.6155,
	urcrnrlat = 41.0476,
	urcrnrlon = 98.4202,
	resolution='l')

m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')
#m.drawcounties(color='darkred')
#m.fillcontinents()
#m.etopo()


plt.title('basemap tutorials')
plt.show()