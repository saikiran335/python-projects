import matplotlib.pyplot as plt

slices=[5,2,7,8]
activities=['sleeping','eating','walking','talking']
cols=['r','b','g','c']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=[0,0.1,0.2,0.3],
        autopct='%1.1f%%')
plt.title('pie chart')
plt.show()
