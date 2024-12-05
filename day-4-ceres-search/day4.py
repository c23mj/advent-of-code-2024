def process_input(path):
    grid = []
    with open(path, 'r') as file:
        for line in file:
            grid.append(line.strip())
    return grid


from collections import deque

def get_all_xmas(grid):
    m, n = len(grid), len(grid[0])
    D = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    next_val = {'X': "M", "M": "A", "A": 'S'}
    total_found = 0


    def search(r, c, direction):
        nonlocal total_found
        frontier = deque([(r, c)])
        
        while frontier:
            a, b = frontier.popleft()
            if grid[a][b] == 'S':
                total_found += 1
                return 
            else:
                dx, dy = direction
                next_a, next_b = a + dx, b + dy
                if 0 <= next_a < m and 0 <= next_b < n and grid[next_a][next_b] == next_val[grid[a][b]]:
                    frontier.append((next_a, next_b))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'X':  
                for direction in D:
                    search(i, j, direction)
                    
    
    return total_found
            

def get_all_x_of_mas(grid):
    m, n = len(grid), len(grid[0])
    D = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    next_val = {"M": "A", "A": 'S'}
    all_A_locs = set()
    x_count = 0

    def search(r, c, direction):
        nonlocal x_count
        frontier = deque([(r, c)])
        dx, dy = direction

        while frontier:
            a, b = frontier.popleft()
            if grid[a][b] == 'S':
                a_loc = (a - dx, b - dy)
                if a_loc in all_A_locs:
                    x_count += 1
                else:
                    all_A_locs.add(a_loc)
            
            else:
                next_a, next_b = a + dx, b + dy
                if 0 <= next_a < m and 0 <= next_b < n and grid[next_a][next_b] == next_val[grid[a][b]]:
                    frontier.append((next_a, next_b))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'M':  
                for direction in D:
                    search(i, j, direction)
    return x_count
        
    

            

if __name__ == "__main__":
    grid = process_input('full_input.txt')
    print(f"total (original) xmas: {get_all_xmas(grid)}")
    print(f"total (x of mas) xmas: {get_all_x_of_mas(grid)}")

