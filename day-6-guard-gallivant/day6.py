def process_input(path):
    grid = []
    starting_pos = (-1, -1)

    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            next_row = []
            for i in range(len(line)):
                next_row.append(line[i])
                if line[i] == '^':
                    starting_pos = len(grid) + 1, i
            grid.append(next_row)

    return grid, starting_pos

            
def simulate_route(grid, starting_pos):
    m, n = len(grid), len(grid[0])

    r, c = starting_pos
    dx, dy = -1, 0
    total_visited = 1
    while 0 <= r < m and 0 <= c < n:
        r, c = r + dx, c + dy
        if 0 <= r < m and 0 <= c < n:
            if grid[r][c] == '#':
                r, c = r - dx, c - dy
                dx, dy = dy, -dx
            elif grid[r][c] == '.':
                total_visited += 1
                grid[r][c] = 'X'
    return total_visited

from tqdm import tqdm

def count_cycles(grid, starting_pos):
    m, n = len(grid), len(grid[0])

    def is_cyclic(grid):
        r, c = starting_pos
        dx, dy = -1, 0
        seen = set()
        while 0 <= r < m and 0 <= c < n:
            r, c = r + dx, c + dy
            if (r, c, dx, dy) in seen:
                return True
            if 0 <= r < m and 0 <= c < n:
                if grid[r][c] == '#':
                    r, c = r - dx, c - dy
                    dx, dy = dy, -dx
            seen.add((r, c, dx, dy))
        return False

    total_cycles = 0
    # Add tqdm to the outer loop
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.':
                grid[i][j] = '#'
                # print(f"calling is_cyclic on obstacle at {(i, j)}")
                if is_cyclic(grid):
                    total_cycles += 1
                grid[i][j] = '.'

    return total_cycles


if __name__ == "__main__":
    grid, starting_pos = process_input('full_input.txt')
    print(f"total # of possible cycles: {count_cycles(grid, starting_pos)}")