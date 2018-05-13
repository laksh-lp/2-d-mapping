from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt 
fig = plt.figure()
ax1 = fig.add_subplot(111,projection = '3d')

x=[1,2,3,4,5,6,7,8,9,10]
y=[4,3,5,7,5,3,7,8,3,5]
z=[9,4,8,3,1,4,6,8,5,7]

x1=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y1=[-4,-3,-5,-7,-5,-3,-7,-8,-3,-5]
z1=[-9,-4,-8,-3,-1,-4,-6,-8,-5,-7]

#ax1.plot_wireframe(x,y,z)
ax1.scatter(x,y,z,c='g',marker='o')
ax1.scatter(x1,y1,z1,c='r',marker='o')

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
