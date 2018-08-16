# Laplace equation numerical solver - FDM
import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------#

# Maximum number of iterations
maxIterations = 500

# Set up a rectangular domain and step delta
lenX = lenY = 100
delta = 1

# Set up Dirichlet boundary conditions
bcTop = 1000
bcBottom = 750
bcLeft = 500
bcRight = 250

# Initial conditions on the interior
icInterior = 0

#-----------------------------------------#

# Set up interpolation and color map for visualization
colorinterpolate = 50
colorMap = plt.cm.jet

# Set up a meshgrid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0,lenY))

#-----------------------------------------#

# Set up the array
V = np.empty((lenX, lenY))
V.fill(icInterior)

# Boundary conditions for the array
V[(lenY-1):, :] = bcTop
V[:1, :] = bcBottom
V[:, (lenX-1):] = bcRight
V[:, :1] = bcLeft

#-----------------------------------------#

# Solve the discrete Laplace equation iteratively (Gauss-Seidel)
print("Iterating, hang on...")
for iteration in range(0, maxIterations):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):
            V[i, j] = 0.25 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])

print("Done.")

#-----------------------------------------#

# Set up the plotting of the solution
plt.title("Electric potential (V) on a 2-D grid")
plt.contourf(X, Y, V, colorinterpolate, cmap=colorMap)

# Add a color bar legend
plt.colorbar()

plt.show()

print("")
