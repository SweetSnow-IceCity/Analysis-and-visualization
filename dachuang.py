import numpy as np
import matplotlib.pyplot as plt

# Parameters
rho = 1.0  # Density
mu = 1.0  # Shear modulus

# Simulation grid
nx = 100  # Number of grid points in x-direction
ny = 100  # Number of grid points in y-direction
dx = 0.1  # Grid spacing in x-direction
dy = 0.1  # Grid spacing in y-direction
dt = 0.01  # Time step size

# Initialize displacement fields
u = np.zeros((nx, ny))  # Displacement field
u_prev = np.zeros((nx, ny))  # Previous time step displacement field

# Main simulation loop
num_steps = 1000
for step in range(num_steps):
    # Update displacement field using finite difference method
    u_next = 2 * u - u_prev + (dt ** 2 / rho) * (mu * laplacian(u, dx, dy))

    # Apply boundary conditions (e.g., fixed boundaries)
    u_next[0, :] = 0  # Example: Fixed boundary at x=0

    # Update previous time step
    u_prev = u
    u = u_next

    # Plot current wavefield
    plt.imshow(u, cmap='coolwarm', extent=[0, nx * dx, 0, ny * dy])
    plt.colorbar()
    plt.title(f"Time step {step}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
