from collections import defaultdict

def process_input(path):
    antennas = defaultdict(list)
    m, n = 0, 0
    with open(path, 'r') as file:
        n = len(file.readline().strip())
        print(f"n = {n}")
        file.seek(0)
        for line in file:
            for col in range(n):
                if line[col] != '.':
                    antennas[line[col]].append((m, col))
            m += 1

    return antennas, m, n

def get_basic_antinode_locs(coords, m, n):
    locs = set()
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            r1, c1 = coords[i]
            r2, c2 = coords[j]
            dx, dy = r1 - r2, c1 - c2
            for temp_r, temp_c in {(r1 + dx, c1 + dy), (r2 - dx, c2 - dy)}:
                if 0 <= temp_r < m and 0 <= temp_c < n:
                    locs.add((temp_r, temp_c))
    return locs

def get_resonant_antinode_locs(coords, m, n):
    locs = set()
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            r1, c1 = coords[i]
            r2, c2 = coords[j]
            dx, dy = r1 - r2, c1 - c2
            
            temp_r, temp_c = r1, c1
            while 0 <= temp_r < m and 0 <= temp_c < n:
                locs.add((temp_r, temp_c))
                temp_r += dx
                temp_c += dy

            temp_r, temp_c = r2, c2
            while 0 <= temp_r < m and 0 <= temp_c < n:
                locs.add((temp_r, temp_c))
                temp_r -= dx
                temp_c -= dy
    return locs


def count_antinodes(antennas, m, n, resonant = False):
    all_antinode_locs = set()
    for _, coords in antennas.items():
        if not resonant:
            all_antinode_locs.update(get_basic_antinode_locs(coords, m, n))
        else:
            all_antinode_locs.update(get_resonant_antinode_locs(coords, m, n))
    return len(all_antinode_locs)



if __name__ == "__main__":
    antennas, m, n = process_input('full_input.txt')
    print(f"total basic antinodes: {count_antinodes(antennas, m, n, False)}")
    print(f"total resonant antinodes: {count_antinodes(antennas, m, n, True)}")