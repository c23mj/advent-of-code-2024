def process_input(path):
    grid = []

    with open(path, 'r') as file:
        for line in file:
            curr_row = []
            for char in line.strip():
                curr_row.append(char)
            grid.append(curr_row)
        
    return grid

from collections import deque, defaultdict

def calculate_fence_costs(grid, discount = False):
    m, n = len(grid), len(grid[0])
    total_cost = 0
    seen = set()
    
    D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def calc_cost(r, c, discount):
        area, perimeter = 0, 0
        sides = defaultdict(set)
        curr_crop = grid[r][c]
        seen.add((r, c))
        frontier = deque([(r, c)])
        while frontier:
            curr_r, curr_c = frontier.popleft()
            area += 1
            # print(f"curr_r, curr_c: {(curr_r, curr_c)}")
            for dx, dy in D:
                a, b = curr_r + dx, curr_c + dy
                if 0 <= a < m and 0 <= b < n and grid[a][b] == curr_crop:
                    if (a, b) not in seen:
                        frontier.append((a, b))
                    seen.add((a, b))
                else:
                    sides[(dx, dy)].add((curr_r, curr_c))
                    perimeter += 1
        
        # count sides
        if discount:
            side_count = 0
            for d, locs in sides.items():
                while locs:
                    rand_item = locs.pop()
                    to_del = {rand_item}
                    # bfs to del all connected items
                    frontier = deque([rand_item])
                    while frontier:
                        curr_r, curr_c = frontier.popleft()
                        for dx, dy in D:
                            a, b = curr_r + dx, curr_c + dy
                            if 0 <= a < m and 0 <= b < n and grid[a][b] == curr_crop:
                                if (a, b) in locs and (a, b) not in to_del:
                                    frontier.append((a, b))
                                    to_del.add((a, b))
                    
                    locs = locs - to_del
                    side_count += 1

        return area * perimeter if not discount else area * side_count


    for i in range(m):
        for j in range(n):
            if (i, j) not in seen:
                total_cost += calc_cost(i, j, discount)
    
    return total_cost

if __name__ == "__main__":
    grid = process_input('full_input.txt')
    print(calculate_fence_costs(grid, False))
    print(calculate_fence_costs(grid, True))





    