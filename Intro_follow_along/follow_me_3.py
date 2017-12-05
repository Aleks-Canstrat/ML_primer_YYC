import numpy as np
import vispy.plot as vplt

fname = '../data/seismic_volume.npy'
data = np.load(fname)
fig = vplt.Fig() 
vol_view = fig[0, 0]  #Divide figure into one view

contrast = True
if contrast:
	clim = [130,200]  # clip the colormap to these data values
	vol_view.volume(data, clim=clim)
else:
	vol_view.volume(data)

fig.show(run=True)