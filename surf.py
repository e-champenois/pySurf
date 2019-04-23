from matplotlib.pyplot import pcolormesh, xlim, ylim, colorbar as cb
from matplotlib.colors import LogNorm
from numpy import concatenate, diff, vstack, hstack, zeros, isfinite

def surf(x, y, z, colorbar=True, log=False, min_over_max=1e-30, **kwargs):

	lx, ly, sz = len(x), len(y), z.shape

	if len(sz)==3:
		if sz[3]==1:
			z = z[:,:,0]
		else:
			raise ValueError('z must be 2-D')

	if lx==sz[0] and ly==sz[1]:
		x, y = y, x
	else:
		assert lx==sz[1] and ly==sz[0], 'x, y, and z array sizes do not match'

	x = concatenate(([(3*x[0]-x[1])/2.],x[:-1]+diff(x)/2.,[(3*x[-1]-x[-2])/2.]))
	y = concatenate(([(3*y[0]-y[1])/2.],y[:-1]+diff(y)/2.,[(3*y[-1]-y[-2])/2.]))
	z = vstack((hstack((z,zeros((z.shape[0],1)))),zeros((1,z.shape[1]+1))))
    
	if log:
		zvals = z[(z>0)&isfinite(z)]
		vmax = zvals.max()
		vmin = max(zvals.min(), vmax*min_over_max)
		norm = LogNorm(vmin=vmin, vmax=vmax)
	else:
		norm=None
    
	plot = pcolormesh(x, y, z, norm=norm, **kwargs)
	xlim(x[[0,-1]])
	ylim(y[[0,-1]])
	if colorbar:
		cb()
	return plot
