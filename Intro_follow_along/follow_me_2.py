import numpy as np
import vispy.plot as vplt

fname = '../data/seismic_volume.npy'
data = np.load(fname)
fig = vplt.Fig() 
scene = fig[0, 0]
scene.volume(data)
fig.show(run=True)