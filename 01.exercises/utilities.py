import math

def is_close(a, b):
    return math.isclose(a, b, abs_tol=1e-6)