import matplotlib.pyplot as plt
import numpy as np

def surf(x, y, z):

	x = np.concatenate(([(3*x[0]-x[1])/2.],x[:-1]+np.diff(x)/2.,[(3*x[-1]-x[-2])/2.]))
	y = np.concatenate(([(3*y[0]-y[1])/2.],y[:-1]+np.diff(y)/2.,[(3*y[-1]-y[-2])/2.]))
	z = np.vstack((np.hstack((z,np.zeros((z.shape[0],1)))),np.zeros((1,z.shape[1]+1))))
	plt.pcolormesh(x, y, z)
	plt.xlim(x[[0,-1]])
	plt.ylim(y[[0,-1]])
	plt.colorbar()
