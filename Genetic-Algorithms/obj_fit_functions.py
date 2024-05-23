from math import cos, sqrt, sin, pi, prod, exp, tan
import numpy as np


# -------------------------------------------------------------------------
# The two Dimensional Griewank's function


def fGriewank(x):  # d = 2
    return (
        (x[0] ** 2 + x[1] ** 2) / 4000 - cos(x[0] / sqrt(2)) * cos(x[1] / sqrt(3)) + 1
    )


# -------------------------------------------------------------------------
# The Griewank's function


def griewank(x):  # d = n
    n = len(x)
    s = sum([xi**2 for xi in x]) / 4000
    p = prod([cos(xi / sqrt(i + 1)) for i, xi in enumerate(x)])
    return 1 + s - p


# ------------------------------------------------------------------------------
# The Michalewicz's function


def michalewicz(x):  # d = n
    m = 10
    n = len(x)
    result = 0
    for i in range(n):
        result -= sin(x[i]) * sin((i + 1) * x[i] ** 2 / pi) ** (2 * m)
    return result


# -------------------------------------------------------------------
# The Rastrigin's Function


def rastrigin(x):  # d = n
    A = 10
    n = len(x)
    sum_term = sum([(xi**2 - A * cos(2 * pi * xi)) for xi in x])
    return A * n + sum_term


# -------------------------------------------------------------------
# The 2 variable Rosenbrock's function


def rosenbrock(x):
    a = 1
    b = 100
    return (a - x[0]) ** 2 + b * (x[1] - x[0] ** 2) ** 2


# --------------------------------------------------------
def fitness_function_1(chromosome):  # d = 3
    x = chromosome[0]
    y = chromosome[1]
    z = chromosome[2]
    fitness = -(x**2 + y**2 + z**2)
    return fitness


# -------------------------------------------
# Booth function


def booth(x):  # d = 2
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2


# ----------------------------------------------------------------
# Bukin function N.6


def bukin_n6(x):  # d = 2
    return 100 * np.sqrt(np.abs(x[1] - 0.01 * x[0] ** 2)) + 0.01 * np.abs(x[0] + 10)


# -------------------------------------------------------------------------------
# Cross-in-Tray function


def cross_in_tray(x):  # d = 2
    return -0.0001 * (
        np.abs(
            np.sin(x[0])
            * np.sin(x[1])
            * np.exp(np.abs(100 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi))
        )
        + 1
    )


# -----------------------------------------------------------------------------------------------------------------------------
# Holder_Table function


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


# ----------------------------------------------------------------------------------------------------
# McCormick function


def mccormick(x):  # d = 2
    return np.sin(x[0] + x[1]) + (x[0] - x[1]) ** 2 - 1.5 * x[0] + 2.5 * x[1] + 1


# ------------------------------
# Poloni's two objective function
def poloni(x):  # !

    A1 = 0.5 * sin(1) - 2 * cos(1) + sin(2) - 1.5 * cos(2)
    A2 = 1.5 * sin(1) - cos(1) + 2 * sin(2) - 0.5 * cos(2)
    B1 = 0.5 * sin(x[0]) - 2 * cos(x[0]) + sin(x[1]) - 1.5 * cos(x[1])
    B2 = 1.5 * sin(x[0]) - cos(x[0]) + 2 * sin(x[1]) - 0.5 * cos(x[1])

    f1 = [1 + (A1 - B1) ** 2 + (A2 - B2) ** 2]
    f2 = [(x[0] + 3) ** 2 + (x[1] + 1) ** 2]
    return [f1, f2]


# -----------------------------------------------------------
# Viennet function
def viennet(x):  # !

    f1 = 0.5 * (x[0] ** 2 + x[1] ** 2) + np.sin(x[0] ** 2 + x[1] ** 2)
    f2 = ((3 * x[0] - 2 * x[1] + 4) / 8) ** 2 + ((x[0] - x[1] + 1) / 27) ** 2 + 15
    f3 = 1 / (x[0] ** 2 + x[1] ** 2 + 1) - 1.1 * exp(-x[0] ** 2 - x[1] ** 2)

    return [f1, f2, f3]


# -------------------------------------------------------------------------
