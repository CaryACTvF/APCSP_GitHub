from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import pyperclip

def genDataWithR(rval,npoints):
	points = ''
	x = np.random.normal(0,1,npoints)
	y = np.random.normal(0,1,npoints)
	a = rval/(1-rval**2)**0.5
	z=a*x+y
	z=z

	for index in range(len(x)):
		points += '\\draw [black, ultra thick] ({},{}) circle [radius=0.05];\n'.format(x[index],z[index])

	slope, intercept, r_value, p_value, std_err = stats.linregress(x,z)
	print('y={}+{} '.format(slope,intercept))
	print('r-value: {}'.format(r_value))

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.scatter(x, z, color='lightblue')
	plt.show()
	return points

# rval = 0.85
# x = np.random.normal(0,1,10)
# y = np.random.normal(0,1,10)
# a = rval/(1-rval**2)**0.5
# z=a*x+y

# for index in range(len(x)):
# 	print('({},{})'.format(x[index],z[index]))

# slope, intercept, r_value, p_value, std_err = stats.linregress(x,z)
# print(r_value)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# # ax.scatter(x, z, color='lightblue')
# plt.show()

points = genDataWithR(0.75,30)
pyperclip.copy(points)