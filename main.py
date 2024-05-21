import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

import operations as op


figure = plt.figure()

ax = figure.add_subplot(111)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    # Define the points of the free-shape object
    verts = [
        (0.3, 0.1),  # left, bottom
        (0.1, 0.9),  # left, top
        (0.9, 0.9),  # right, top
        (0.9, 0.1),  # right, bottom
        (0.5, 0.5),  # back to the middle
        (0.3, 0.1),
    ]
    # Define the path codes
    codes = [Path.MOVETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.LINETO,
             Path.CLOSEPOLY,
             ]
    # Create a path
    path = Path(verts, codes)
    # Create a patch
    patch = patches.PathPatch(path, facecolor='red', lw=1)
    # Add the patch to the Axes
    ax.add_patch(patch)
    plt.xlim([0, 1])
    plt.ylim([0, 1])

    # Display the figure
    plt.show()

if __name__ == "__main__":
    main()
