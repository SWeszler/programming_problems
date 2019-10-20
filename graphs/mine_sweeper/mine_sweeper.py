def mine_sweeper(bombs, num_rows, num_cols):
    """Assigns correct numbers in a field of Minesweeper, 
    which is represented as two-dimensional list."""

    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb in bombs:
        field[bomb[0]][bomb[1]] = -1
        for i in range(bomb[0] - 1, bomb[0] + 2):
            for j in range(bomb[1] - 1, bomb[1] + 2):
                if (0 <= i < num_rows and 0 <= j < num_cols 
                and field[i][j] != -1):
                    field[i][j] += 1

    return field


def count_bombs_around(row, col, field):
    """Counts bombs in a field around each cell"""

    count = 0

    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            try:
                if field[i][j] == -1 and i >= 0 and j >= 0:
                    count += 1
            except:
                pass

    return count

def mine_sweeper_naive(bombs, num_rows, num_cols):
    """NAIVE approach, not recommended.
    Assigns correct numbers in a field of Minesweeper, 
    which is represented as two-dimensional list."""
    
    #preparing field
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    #distributing bombs
    for bomb in bombs:
        field[bomb[0]][bomb[1]] = -1

    #count bombs around each cell
    for i in range(num_rows):
        for j in range(num_cols):
            if field[i][j] != -1:
                field[i][j] = count_bombs_around(i, j, field)

    return field

