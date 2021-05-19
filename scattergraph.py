import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[7,6,5,4,3,2,1]

plt.scatter(x,y, label='cat', color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('scatter graph')
plt.legend()
plt.show()
