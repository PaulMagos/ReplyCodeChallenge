import numpy as np

def max_cells(mat : np.array):

    points = []

    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            points.append((i, j, mat[i, j]))

    points.sort(key=lambda x : x[2], reverse=True)

    return points


