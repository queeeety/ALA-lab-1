import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin
import cv2 as cv
import time

figure = plt.figure()

ax = figure.add_subplot(111)


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def VisualisatorOfTheVector(verts):
    # Unzip the vertices into x and y coordinates
    # try:
    x, y = zip(*verts)
    # except ValueError:
    #     verts = [(vert[0], vert[1]) for vert in verts]
    #     x, y = zip(*verts)
    # Add the first point to the end to close the polygon
    x = x + (x[0],)
    y = y + (y[0],)
    # Plot the polygon
    plt.plot(x, y, 'r-')
    maxlimitX = max(x) + 1
    minlimitX = min(x) - 1
    maxlimitY = max(y) + 1
    minlimitY = min(y) - 1

    plt.xlim([minlimitX, maxlimitX])
    plt.ylim([minlimitY, maxlimitY])
    # Display the figure
    plt.show()
    return 0


def Multiplier(verts, i, j):
    output = []
    for vert in verts:
         output.append((vert[0] * i.x + vert[1] * j.x, vert[0] * i.y + vert[1] * j.y))
    return output


def funcMultiplier(verts, matrix):
    output = []
    for vert in verts:
        output.append((vert[0] * matrix[0][0] + vert[1] * matrix[0][1], vert[0] * matrix[1][0] + vert[1] * matrix[1][1]))
    return output


def main():
    # Define the points of the free-shape object
    global mirror_matrix, tilt_matrix
    verts1 = [
        (0.0, 0.0),  # left, bottom
        (0.1, 0.9),  # left, top
        (0.9, 0.9),  # right, top
        (0.9, 0.1),  # right, bottom
        (0.5, 0.5),  # back to the middle
        (0.3, 0.1),
    ]
    verts2 = [
        (0.0, 0.0),  # left, bottom
        (1.0, 5.0),  # left, top
        (5.0, 5.0),  # right, top
        (5.0, 9.0),  # right, bottom
        (8.0, 7.0),  # back to the middle
        (10, 3),
    ]

    whatFigure = input("Choose the figure (1 - idk, some strange thing, 2 - another strange thing): ")
    if whatFigure == '1':
        start_verts = verts1
    elif whatFigure == '2':
        start_verts = verts2
    else:
        print("Incorrect figure number. I will choose the first one.")
        start_verts = verts1

    VisualisatorOfTheVector(start_verts)

    i = Node(1, 0)
    j = Node(0, 1)
    print("The figures are displayed.")
    while True:
        print("""Choose the operation:
        1. Rotation
        2. Scaling
        3. Mirroring
        4. Tilt axes
        5. Custom matrix transformation
        6. Use external library 
        7. Image transformationl
        """)
        operation = input("Enter the operation number: ")
        match (operation):
            case '1':
                anglestr = input("Enter the angle of rotation (clockwise): ")
                while True:
                    try:
                        angle = float(anglestr)
                        break
                    except ValueError:
                        anglestr = input("Enter the angle of rotation (clockwise): ")

                # Rotate the vectors
                new_i_x = i.x * np.cos(np.radians(angle)) - i.y * np.sin(np.radians(angle))
                new_i_y = i.x * np.sin(np.radians(angle)) + i.y * np.cos(np.radians(angle))
                i.x, i.y = new_i_x, new_i_y
                new_j_x = j.x * np.cos(np.radians(angle)) - j.y * np.sin(np.radians(angle))
                new_j_y = j.x * np.sin(np.radians(angle)) + j.y * np.cos(np.radians(angle))
                j.x, j.y = new_j_x, new_j_y

                new_verts = Multiplier(start_verts, i, j)
                VisualisatorOfTheVector(new_verts)

            case '2':
                scalestr = input("Enter the scale factor: ")
                while True:
                    try:
                        scale = float(scalestr)
                        break
                    except ValueError:
                        scalestr = input("Enter the scale factor: ")

                i.x *= scale
                i.y *= scale
                j.x *= scale
                j.y *= scale

                new_verts = Multiplier(start_verts, i, j)
                VisualisatorOfTheVector(new_verts)

            case '3':
                answer = input("Enter the axis of mirroring (x or y): ")
                while answer != 'x' and answer != 'y':
                    answer = input("Enter the correct axis of mirroring (x or y): ")
                if answer == 'x':
                    j.x *= -1
                    i.x *= -1
                elif answer == 'y':
                    j.y *= -1
                    i.y *= -1
                VisualisatorOfTheVector(Multiplier(start_verts, i, j))

            case '4':
                tilt_axis = input("Enter the axis to tilt (x or y): ")
                while tilt_axis != 'x' and tilt_axis != 'y':
                    tilt_axis = input("Enter the correct axis to tilt (x or y): ")

                tilt_angle_str = input("Enter the tilt angle: ")
                while True:
                    try:
                        tilt_angle = float(tilt_angle_str)
                        break
                    except ValueError:
                        tilt_angle_str = input("Enter the tilt angle: ")

                if tilt_axis == 'x':
                    # Tilt the i vector
                    new_i_x = i.x * np.cos(np.radians(tilt_angle)) - i.y * np.sin(np.radians(tilt_angle))
                    new_i_y = i.x * np.sin(np.radians(tilt_angle)) + i.y * np.cos(np.radians(tilt_angle))
                    i.x, i.y = new_i_x, new_i_y
                elif tilt_axis == 'y':
                    # Tilt the j vector
                    new_j_x = j.x * np.cos(np.radians(tilt_angle)) - j.y * np.sin(np.radians(tilt_angle))
                    new_j_y = j.x * np.sin(np.radians(tilt_angle)) + j.y * np.cos(np.radians(tilt_angle))
                    j.x, j.y = new_j_x, new_j_y
                    new_verts = Multiplier(start_verts, i, j)
                    VisualisatorOfTheVector(new_verts)
            case '5':
                    print("Right now you will be able to enter the tranformation matrix.")
                    print("The matrix should be like this:")
                    print("a b")
                    print("c d")

                    while True:
                        try:
                            a = float(input("Enter the a coefficient: "))
                            b = float(input("Enter the b coefficient: "))
                            c = float(input("Enter the c coefficient: "))
                            d = float(input("Enter the d coefficient: "))
                            break
                        except ValueError:
                            print("Incorrect input. Try again.")
                    i.x, i.y = a, c
                    j.x, j.y = b, d
                    new_verts = Multiplier(start_verts, i, j)
                    VisualisatorOfTheVector(new_verts)

            case '6':
                verts = start_verts
                while True:
                    print("Choose the operation:")
                    print("1. Rotation")
                    print("2. Scaling")
                    print("3. Mirroring")
                    print("4. Tilt axes")
                    print("5. Custom matrix transformation")
                    print("6. Exit")
                    b = input("Enter the operation number: ")
                    match b:

                        case "1":
                            angle = float(input("Enter the angle of rotation (clockwise): "))
                            rotated_matrix = cv.getRotationMatrix2D((0, 0), angle, 1)
                            verts = funcMultiplier(verts, rotated_matrix)
                            VisualisatorOfTheVector(verts)

                        case "2":
                            scale = float(input("Enter the scale factor: "))
                            scale_matrix = np.array([[scale, 0], [0, scale]])
                            verts = funcMultiplier(verts, scale_matrix)
                            VisualisatorOfTheVector(verts)

                        case "3":
                            axis = input("Enter the axis of mirroring (x or y): ")
                            if axis == 'x':
                                mirror_matrix = np.array([[-1, 0], [0, 1]])
                            elif axis == 'y':
                                mirror_matrix = np.array([[1, 0], [0, -1]])
                            verts = funcMultiplier(verts, mirror_matrix)
                            VisualisatorOfTheVector(verts)

                        case "4":
                            axis = input("Enter the axis to tilt (x or y): ")
                            tilt_angle = float(input("Enter the tilt angle: "))

                            if axis == 'x':
                                tilt_matrix = np.array([[cos(tilt_angle), sin(tilt_angle)], [sin(tilt_angle), cos(tilt_angle)]])
                            elif axis == 'y':
                                tilt_matrix = np.array([[cos(tilt_angle), -sin(tilt_angle)], [sin(tilt_angle), cos(tilt_angle)]])
                            verts = funcMultiplier(verts, tilt_matrix)
                            VisualisatorOfTheVector(verts)

                        case "5":
                            matrix = np.array([[float(input("Enter the a coefficient: ")), float(input("Enter the b coefficient: "))],
                                               [float(input("Enter the c coefficient: ")), float(input("Enter the d coefficient: "))]])
                            verts = funcMultiplier(verts, matrix)
                            VisualisatorOfTheVector(verts)
                        case '6':
                            break

            case '7':
                img = cv.imread("image.jpg")
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                plt.imshow(img)
                plt.show()
                time.sleep(3)

                # Get the image shape
                (h, w) = img.shape[:2]

                # Define the center of the image
                center = (w / 2, h / 2)

                # Define the angle of rotation
                angle = 45  # Rotate the image by 45 degrees

                # Get the rotation matrix
                M = cv.getRotationMatrix2D(center, angle, 1.0)

                # Perform the rotation
                rotated = cv.warpAffine(img, M, (w, h))

                # Display the rotated image
                img2 = cv.cvtColor(rotated, cv.COLOR_BGR2RGB)
                plt.imshow(img2)
                plt.show()

                # # Display the rotated image
                # cv.imshow('Rotated Image', rotated)
                # cv.waitKey(0)
                # cv.destroyAllWindows()

                time.sleep(3)

                # Load the image
                img = cv.imread('image.jpg')

                # Get the image shape
                (h, w) = img.shape[:2]

                # Define the new width
                new_w = w // 2

                # Resize the image
                resized = cv.resize(img, (new_w, h))

                # Display the resized image
                img2 = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
                plt.imshow(img2)
                plt.show()

            case _:
                print("Incorrect operation number.")





if __name__ == "__main__":
    main()
