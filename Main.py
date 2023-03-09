from input_reader import read_input
from snake import Snake
from starting_cells import max_cells
from print_output import print_output

import numpy as np

def main():
    mat, n_snake, snakes_lenght, wormholes = read_input("./inputs/06-input-reply-running-man.txt")
    fixed_mat = np.copy(mat)
    punti_ordinati = max_cells(mat=mat)
    # lista di tuple (i, j, valore)

    snakes = []
    k = 0
    for i in range(n_snake):

        while mat[punti_ordinati[k][0], punti_ordinati[k][1]] == -10002:
            k += 1

        row = punti_ordinati[k][0]
        col = punti_ordinati[k][1]

        snake = Snake(startCell=(row, col), len=snakes_lenght[i], mat=mat)

        j = 0
        while j < snakes_lenght[i] - 1:
            m, p = snake.greedy_move(mat)
            if not m:
                break
            snake.move(m)
            mat[p] = -10002
            j += 1

        if j == snakes_lenght[i] - 1:
            snakes.append(snake)
        else:
            snakes.append(None)
    print(snakes)

    print_output(snakes, "./outputs/out7.txt")


        
    print("Hello World")

if __name__ == "__main__":
    main()

    

