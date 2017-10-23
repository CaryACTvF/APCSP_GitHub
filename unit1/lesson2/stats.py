from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.random.random(100)
y = np.random.random(100)

for index in range(len(x)):
	print('({},{})'.format(x[index],y[index]))

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print(r_value)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, color='lightblue')
plt.show()
