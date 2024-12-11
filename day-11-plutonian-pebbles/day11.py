def process_input(path):
    with open(path, 'r') as file:
        line = file.readline()
        return list(map(int, line.strip().split()))
    

# naive brute force
# def count_after_blinks(num_blinks: int, stones):
#     next_stones = []
#     for _ in range(num_blinks):
#         print(f"blink {_}")
#         next_stones = []
#         for stone in stones:
#             stone_res = change_stone(stone)
#             next_stones.extend(stone_res)
#         stones = next_stones
#     return len(next_stones)

import functools
@functools.cache
def change_stone(stone):
    if stone == 0:
        return [1]
    
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        left = int(stone_str[:len(stone_str)//2])
        right =  int(stone_str[len(stone_str)//2:])
        return [left, right]

    return [stone * 2024]

# memoize a bit better lol
from collections import Counter
def count_after_blinks(num_blinks: int, stones):
    stones = Counter(stones)
    next_stones = Counter()
    for _ in range(num_blinks):
        next_stones = Counter()
        for stone, count in stones.items():
            changed = change_stone(stone)
            for new_stone in changed:
                next_stones[new_stone] += count

        stones = next_stones
    return sum(next_stones.values())

if __name__ == "__main__":
    stones = process_input('full_input.txt')
    print(count_after_blinks(25, stones))
    print(count_after_blinks(75, stones))

 



    