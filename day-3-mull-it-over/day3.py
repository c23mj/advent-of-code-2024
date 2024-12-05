def process_input(path):
    lists = []
    with open(path, 'r') as file:
        for line in file:
            lists.append(line)
    return ''.join(lists)

import re
def get_exprs(s: str):
    pattern = r"mul\(\d{1,3},\s?\d{1,3}\)|do\(\)|don't\(\)"
    # Find all matches
    matches = re.findall(pattern, s)
    return matches

def process_muls(exprs):
    pattern = r"mul\((\d{1,3}),\s?(\d{1,3})\)"
    res = 0
    for expr in exprs:
        match = re.match(pattern, expr)
        if match:
            x, y = map(int, match.groups())  
            prod = x * y
            res += prod
    return res


def process_exprs(exprs):
    pattern = r"mul\((\d{1,3}),\s?(\d{1,3})\)"
    res = 0
    count_mul = True
    for expr in exprs:
        if expr == 'do()':
            count_mul = True
        elif expr == 'don\'t()':
            count_mul = False
        elif count_mul:
            match = re.match(pattern, expr)
            x, y = map(int, match.groups())  
            prod = x * y
            res += prod
    return res

if __name__ == "__main__":
    s = process_input('full_input.txt')
    exprs = get_exprs(s)
    print(f"Processed result without do/don't: {process_muls(exprs)}")
    print(f"Processed result with do/don't: {process_exprs(exprs)}")

