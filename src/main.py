import numpy as np


def my_sum(a, b):
    return a + b


def vec_diff_length(a, b):
    return np.linalg.norm(a - b)


if __name__ == "__main__":
    print(my_sum(5, 10))
    print(vec_diff_length(np.array([1, 1]), np.array([2, 2])))
    
    print("docerisation example")
