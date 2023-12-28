import cv2
import numpy as np
import math

image = cv2.imread("angle.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 57, None, 0, 0)
image_with_lines = image.copy()


intersection_points = []

if lines is not None:
    for i in range(len(lines)):
        rho, theta = lines[i][0]
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a * rho, b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv2.line(image_with_lines, pt1, pt2, (0, 255, 0), 2)


        for j in range(i + 1, len(lines)):
            rho1, theta1 = lines[i][0]
            rho2, theta2 = lines[j][0]

            # Calculate intersection point only if lines are not parallel
            if np.abs(theta1 - theta2) > np.pi / 180.0:
                A = np.array([[np.cos(theta1), np.sin(theta1)],
                              [np.cos(theta2), np.sin(theta2)]])
                B = np.array([[rho1], [rho2]])
                intersection_point = np.linalg.solve(A, B)

                # Print intersection points to the terminal
                print(f"Intersection Point {len(intersection_points) + 1}: ({intersection_point[0]}, {intersection_point[1]})")

                # Convert intersection_point to tuple for comparison
                intersection_point_tuple = (int(intersection_point[0]), int(intersection_point[1]))

                # Avoid duplicate points
                if intersection_point_tuple not in intersection_points:
                    intersection_points.append(intersection_point_tuple)

                    # Draw intersection point on the image
                    cv2.circle(image_with_lines, intersection_point_tuple, 5, (0, 0, 255), -1)


# Consider points 2 and 4
if len(intersection_points) >= 3:
    x1, y1 = intersection_points[1]
    x4, y4 = intersection_points[3]
    # Draw line connecting points 
    cv2.line(image_with_lines, (x1, y1), (x4, y4), (0, 0,255 ), 2)

# Calculate slope and arc tangent
    if {x4 - x1} != 0:
        slope = abs(y4 - y1) / abs(x4 - x1)
        print(f"Slope for points ({x1}, {y1}) - ({x4}, {y4}): {slope}")

        # Calculate arc tangent (inverse tangent) in degrees
        angle_radians = np.arctan(slope)
        angle_degrees = np.degrees(angle_radians)
        print(f"Arc tangent (degrees): {angle_degrees}")
        # Draw text annotation with slope and arc tangent
        text_slope = f"Angle: {angle_degrees:.2f} degrees"
        cv2.putText(image_with_lines, text_slope, (min(x1, x4) + 10, min(y1, y4) - 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
cv2.imshow("Image", image_with_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()