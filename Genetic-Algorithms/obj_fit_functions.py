from math import cos, sqrt, sin, pi, prod, exp, tan
import numpy as np


# -------------------------------------------------------------------------
# The two Dimensional Griewank's function


from math import cos, sqrt, sin, pi, prod, exp
import numpy as np


# The fitness function for fGriewank
def fGriewank(x):  # d = 2
    return (
        (x[0] ** 2 + x[1] ** 2) / 4000 - cos(x[0] / sqrt(2)) * cos(x[1] / sqrt(3)) + 1
    )


# The fitness function for Griewank
def griewank(x):  # d = n
    n = len(x)
    s = sum([xi**2 for xi in x]) / 4000
    p = prod([cos(xi / sqrt(i + 1)) for i, xi in enumerate(x)])
    return 1 + s - p


# The fitness function for Michalewicz
def michalewicz(x):  # d = n
    m = 10
    n = len(x)
    result = 0
    for i in range(n):
        result -= sin(x[i]) * sin((i + 1) * x[i] ** 2 / pi) ** (2 * m)
    return result


# The fitness function for Rastrigin
def rastrigin(x):  # d = n
    A = 10
    n = len(x)
    sum_term = sum([(xi**2 - A * cos(2 * pi * xi)) for xi in x])
    return A * n + sum_term


# The fitness function for Booth
def booth(x):  # d = 2
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2


# The fitness function for Bukin_n6
def bukin_n6(x):  # d = 2
    return 100 * np.sqrt(np.abs(x[1] - 0.01 * x[0] ** 2)) + 0.01 * np.abs(x[0] + 10)


# The fitness function for Cross-in-Tray
def cross_in_tray(x):  # d = 2
    return -0.0001 * (
        np.abs(
            np.sin(x[0])
            * np.sin(x[1])
            * np.exp(np.abs(100 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi))
        )
        + 1
    )


# The fitness function for Holder_Table
def holder_table(x):  # d = 2
    num = -np.abs(
        np.sin(x[0])
        * np.cos(x[1])
        * np.exp(np.abs(1 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi))
        * np.exp(np.abs(1 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi))
    )
    den = 1 + np.abs(x[0] + x[1]) * np.exp(
        np.abs(1 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi)
    )
    return num / den


# The fitness function for McCormick
def mccormick(x):  # d = 2
    return np.sin(x[0] + x[1]) + (x[0] - x[1]) ** 2 - 1.5 * x[0] + 2.5 * x[1] + 1


# The fitness function for Poloni
def poloni(x):  # !

    A1 = 0.5 * sin(1) - 2 * cos(1) + sin(2) - 1.5 * cos(2)
    A2 = 1.5 * sin(1) - cos(1) + 2 * sin(2) - 0.5 * cos(2)
    B1 = 0.5 * sin(x[0]) - 2 * cos(x[0]) + sin(x[1]) - 1.5 * cos(x[1])
    B2 = 1.5 * sin(x[0]) - cos(x[0]) + 2 * sin(x[1]) - 0.5 * cos(x[1])

    f1 = [1 + (A1 - B1) ** 2 + (A2 - B2) ** 2]
    f2 = [(x[0] + 3) ** 2 + (x[1] + 1) ** 2]
    return [f1, f2]


# The fitness function for Viennet
def viennet(x):  # !

    f1 = 0.5 * (x[0] ** 2 + x[1] ** 2) + np.sin(x[0] ** 2 + x[1] ** 2)
    f2 = ((3 * x[0] - 2 * x[1] + 4) / 8) ** 2 + ((x[0] - x[1] + 1) / 27) ** 2 + 15
    f3 = 1 / (x[0] ** 2 + x[1] ** 2 + 1) - 1.1 * exp(-x[0] ** 2 - x[1] ** 2)

    return [f1, f2, f3]


# -------------------------------------------------------------------------
