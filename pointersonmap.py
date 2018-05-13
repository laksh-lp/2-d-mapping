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
xs=[]
ys=[]

nyclat,nyclon = 13.5840,76.5034
xpt, ypt = m(nyclon,nyclat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt,ypt,'g^',markersize=15)

lalat,lalon = 24.5091,84.8860
xpt,ypt = m(lalon,lalat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt,ypt,'g^',markersize=15)

m.plot(xs,ys,color='r',linewidth=3,label="patanahi")

print xs



plt.title('basemap tutorials')
plt.show()