import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time


def rotation_matrix(axis, theta):
    axis = np.asarray(axis)
    axis = axis / np.sqrt(np.dot(axis, axis))
    a = np.cos(theta / 2.0)
    b, c, d = -axis * np.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


def mirror_by_x(x, y, z):
    mirror_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    mirrored_x = []
    mirrored_y = []
    mirrored_z = []
    for i in range(len(x)):
        vert_array = np.array([x[i], y[i], z[i]])
        transformed_vert = np.dot(mirror_matrix, vert_array)
        mirrored_x.append(transformed_vert[0])
        mirrored_y.append(transformed_vert[1])
        mirrored_z.append(transformed_vert[2])
    return mirrored_x, mirrored_y, mirrored_z


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [0, 1, 2, 3, 4, 0]
y = [0, 0, 2, 1, 5, 0]
z = [0, 0, 1, 3, 3, 0]

ax.plot3D(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

time.sleep(3)

x, y, z = mirror_by_x(x, y, z)

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

ax2.plot3D(x, y, z, c='r', marker='o')

ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
ax2.set_zlabel('Z Label')

plt.show()

time.sleep(3)

# Define rotation axis and angle
axis = [0, 0, 1]  # Rotate around z-axis
theta = np.radians(30)  # Rotate by 30 degrees

# Create rotation matrix
R = rotation_matrix(axis, theta)

# Apply rotation to each vertex
rotated_x, rotated_y, rotated_z = [], [], []
for i in range(len(x)):
    rotated_vert = np.dot(R, [x[i], y[i], z[i]])
    rotated_x.append(rotated_vert[0])
    rotated_y.append(rotated_vert[1])
    rotated_z.append(rotated_vert[2])

# Plot the rotated figure
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')
ax3.plot3D(rotated_x, rotated_y, rotated_z, c='r', marker='o')
ax3.set_xlabel('X Label')
ax3.set_ylabel('Y Label')
ax3.set_zlabel('Z Label')
plt.show()


