import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis
import warnings

def compute_mandelbrot(N_max, some_threshold, nx, ny):
    #2D Array of points (x,y)
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)
    #Corresponding complex value c
    c = x[:,newaxis] + 1j*y[newaxis,:]

    # Mandelbrot iteration to store the c grid in z 
    z = c

    #Suppresses warnings from overflows in the grid
    warnings.filterwarnings("ignore")
    
    #Applying the mandelbrot iteration for N_max 
    for j in range(N_max):
            z = z**2 + c
            
    #Creates a 2D boolean matrix mask to check if
    #|z| < threshold
    mask = (abs(z) < some_threshold)

    return mask

#Calls the mandelbrot function
mask = compute_mandelbrot(50, 50., 601, 401)

#Plotting/Saving the image as a mandelbrot.png
plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.show()