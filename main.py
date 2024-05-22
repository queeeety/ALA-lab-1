import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
from math import cos, sin
import operations as op


figure = plt.figure()

ax = figure.add_subplot(111)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def VisualisatorOfTheVector(verts):
    # Unzip the vertices into x and y coordinates
    x, y = zip(*verts)
    # Add the first point to the end to close the polygon
    x = x + (x[0],)
    y = y + (y[0],)
    # Plot the polygon
    plt.plot(x, y, 'r-')
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    # Display the figure
    plt.show()
    return 0
def VisualisatorOfTheObject(verts, codes):
    # Create a path
    path = Path(verts, codes)
    # Create a patch
    patch = patches.PathPatch(path, facecolor='red', lw=1)
    # Add the patch to the Axes
    ax.add_patch(patch)
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])

    # Display the figure
    plt.show()
    return 0



def main():
    # Define the points of the free-shape object
    start_verts = [
        (0.3, 0.1),  # left, bottom
        (0.1, 0.9),  # left, top
        (0.9, 0.9),  # right, top
        (0.9, 0.1),  # right, bottom
        (0.5, 0.5),  # back to the middle
        (0.3, 0.1),
    ]
    # Define the path codes
    start_codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]

    VisualisatorOfTheObject(start_verts, start_codes)

    i = Node(1, 0)
    j = Node(0, 1)
    print("The figures are displayed.")
    print("""Choose the operation:
    1. Rotation
    2. Left rotation
    3. Scaling
    4. Mirroring
    5. Tilt axes
    6. Matrix tilt
    """)

    VisualisatorOfTheVector([(0, 0), (i.x, i.y)])

    operation = input("Enter the operation number: ")
    match (operation):
        case '1':
            angle = int(input("Enter the angle of rotation (clockwise): "))

            # Rotate the vectors
            new_i_x = i.x * np.cos(np.radians(angle)) - i.y * np.sin(np.radians(angle))
            new_i_y = i.x * np.sin(np.radians(angle)) + i.y * np.cos(np.radians(angle))
            i.x, i.y = new_i_x, new_i_y

            new_j_x = j.x * np.cos(np.radians(angle)) - j.y * np.sin(np.radians(angle))
            new_j_y = j.x * np.sin(np.radians(angle)) + j.y * np.cos(np.radians(angle))
            j.x, j.y = new_j_x, new_j_y

            VisualisatorOfTheVector([(0, 0), (i.x, i.y)])
            VisualisatorOfTheVector([(0, 0), (j.x, j.y)])

            print(i.x == i.y)
            print(j.x == j.y)
            print(i.x == np.sqrt(2))
        # case '2':
        #
        # case '3':
        #
        # case '4':
        #
        # case '5':
        #
        # case '6':
        #
        # case _:
        #     print("Incorrect operation number.")





if __name__ == "__main__":
    main()
