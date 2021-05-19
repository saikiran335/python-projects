import matplotlib.pyplot as plt

days=[1,2,3,4,5,6]

sleeping=[2,4,6,8,0,4]
eating=[9,8,7,9,8,9]
walking=[7,8,5,9,6,7]
talking=[9,8,7,6,7,5]
plt.plot([],[],color='r',label='sleeping',linewidth=5)
plt.plot([],[],color='b',label='eating',linewidth=5)
plt.plot([],[],color='g',label='walking',linewidth=5)
plt.plot([],[],color='k',label='talking',linewidth=5)


plt.stackplot(days,sleeping,eating,walking,talking,colors=['r','b','g','k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('area graph')
plt.legend()
plt.show()
