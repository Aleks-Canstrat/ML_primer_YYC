"""
In this exercise we are going to make a simple topography 
map from a digitial elevation model in 5 lines of code
"""

# Step 1: import numpy and matplotlib libraries

import numpy as np
import matplotlib.pyplot as plt

# Step 2: Load topography data into numpy array

data = np.load('../data/topography.npy')

# Step 3: call the imshow function on the data
plt.imshow(data, cmap='summer')

# Show the figure to a figure window on the screen
# (close the window when you are done)
plt.show() 

# And then it will save the figure to a file (optional)
plt.savefig('images/topography.png')
