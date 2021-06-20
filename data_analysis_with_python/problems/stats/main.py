import numpy as np


def calculate(list):
    """ Trasforms list of 9 numbers to 3.3 matrix, returns a collection of basic stats related to the matrix
    Args: 
        list (list): List of 9 numbers
    Raises: 
        ValueError: When the list is not nine numbers
    Returns: 
        Dictionary: 
            keys: basic stats 
            values: array of axis 0 values, array of axis 1 values, flatten values
    """

    try:
        arr = np.array(list).reshape((3,3))
    except ValueError:
        raise ValueError('List must contain nine numbers.')

    stats_list = {
        'mean': arr.mean,
        'variance': arr.var,
        'standard deviation': arr.std,
        'max': arr.max,
        'min': arr.min,
        'sum': arr.sum,
    }

    calculations = {}

    for stat, func in stats_list.items():
        calculations[stat] = [
            func(axis=0).tolist(),
            func(axis=1).tolist(),
            func()
        ]

    return calculations
