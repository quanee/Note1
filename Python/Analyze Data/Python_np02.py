import numpy as np


x2d = np.array(((100, 200, 300),
                (111, 222, 333),
                (123, 456, 789),
                (125, 457, 791),
                (127, 459, 793),
                (129, 461, 795)))

print(x2d)
x2d.ravel()
print(x2d)
x2d.resize((3, 6))
print(x2d)
x2d.reshape(6, 3)