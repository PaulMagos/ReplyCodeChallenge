
def print_output(snakes, file_name):
    with open(file_name, "w") as file:
        for snake in snakes:
            if not snake:
                print(file=file)
                continue
            print(snake.startCell[1], snake.startCell[0], sep=" ", end=" ", file=file)
            for m in snake.moves:
                print(m, end=" ", file=file)
            print(file=file)
