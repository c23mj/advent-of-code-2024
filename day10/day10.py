def process_input(path):
    grid = []

    with open(path, 'r') as file:
        for line in file:
            curr_row = []
            for char in line.strip():
                if char.isdigit():
                    curr_row.append(int(char))
                else:
                    curr_row.append(float('inf'))

            grid.append(curr_row)
        
    return grid

from collections import deque

def count_trail_scores(grid):
    m, n = len(grid), len(grid[0])
    starts = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                starts.add((i, j))
    
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def calc_score(r, c):
        score = 0
        seen = {(r, c)}
        frontier = deque([(r, c)])
        while frontier:
            curr_r, curr_c = frontier.popleft()
            curr_val = grid[curr_r][curr_c]
            # print(f"curr_r, curr_c, curr_val {(curr_r, curr_c, curr_val)}")

            if curr_val == 9:
                score += 1
                continue
            for dx, dy in D:
                a, b = curr_r + dx, curr_c + dy
                if 0 <= a < m and 0 <= b < n and grid[a][b] - grid[curr_r][curr_c] == 1 and (a, b) not in seen:
                    seen.add((a, b))
                    frontier.append((a, b))
        
        return score

    total_score = 0
    for start_r, start_c in starts:
        total_score += calc_score(start_r, start_c)
    
    return total_score

from collections import defaultdict
def count_trail_ratings(grid):
    m, n = len(grid), len(grid[0])
    starts = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                starts.add((i, j))
    
    # print(f"starts: {starts}")

    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def calc_rating(r, c):
        reachable_ends = set()
        memo = [[0 for _ in range(n)] for __ in range(m)]
        memo[r][c] = 1
        frontier = deque([(r, c)])
        count = 0
        while frontier:
            count += 1
            level_len = len(frontier)
            seen = set()
            for _ in range(level_len):
                curr_r, curr_c = frontier.popleft()
                curr_val = grid[curr_r][curr_c]
                if curr_val == 9:
                    reachable_ends.add((curr_r, curr_c))
                    continue
                for dx, dy in D:
                    a, b = curr_r + dx, curr_c + dy
                    if 0 <= a < m and 0 <= b < n and grid[a][b] - grid[curr_r][curr_c] == 1:
                        if (a, b) not in seen:
                            frontier.append((a, b))
                            seen.add((a, b))
                        memo[a][b] += memo[curr_r][curr_c]
        return sum(memo[r][c] for r, c in reachable_ends)

    total_score = 0
    for start_r, start_c in starts:
        total_score += calc_rating(start_r, start_c)
    
    return total_score

    

    

if __name__ == "__main__":
    grid = process_input('full_input.txt')
    print(count_trail_scores(grid))
    print(count_trail_ratings(grid))



    