def click(field, num_rows, num_cols, given_i, given_j):
    """Returns a field with revealed all 0 cells connected to the clicked one.
    Revealed cell is represented by -2"""
    
    import queue
    to_check = queue.Queue()
    if field[given_i][given_j] == 0:
        field[given_i][given_j] = -2
        to_check.put((given_i, given_j))
    else:
        return field

    while not to_check.empty():
        (current_i, current_j) = to_check.get()
        for i in range(current_i - 1, current_i + 2):
            for j in range(current_j - 1, current_j + 2):
                if (0 <= i < num_rows and 0 <= j < num_cols
                        and field[i][j] == 0):
                    field[i][j] = -2
                    to_check.put((i, j))
    return field