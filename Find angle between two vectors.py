import numpy as np
import math
pi = math.pi


def getAngle(vector1, vector2):
    dt = np.dot(vector1, vector2)
    return np.arccos(dt/(np.linalg.norm(vector1)*np.linalg.norm(vector2)))*(180/pi)


# Find angle between two vectors

a = [1, 0, 3]
b = [5, 5, 0]

print("Angle Between a and b is {} degree".format(getAngle(a, b)))
