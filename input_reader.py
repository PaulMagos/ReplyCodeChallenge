import numpy as np


def read_input(path):
    with open(path, "r") as file :
        line_1 = next(file)
        line_2 = next(file)
        
        wormholes = []
        
        splitted_line_1 = line_1.split(" ")
        C = int(splitted_line_1[0])
        R = int(splitted_line_1[1])
        n_snakes = int(splitted_line_1[2])

        snakes_lenght = [int(i) for i in line_2.split(" ")]
        

        mat = np.ndarray(shape=(R, C), dtype=int)
        for i in range(R):
            for j, cell in enumerate(next(file).split(" ")):
                if cell.endswith("\n"):
                    cell = cell[:-1]
                if cell.isnumeric():
                    mat[i, j] = int(cell)
                else:
                    mat[i, j] = -10001
                    wormholes.append((i,j))

        return mat, n_snakes, snakes_lenght, wormholes

