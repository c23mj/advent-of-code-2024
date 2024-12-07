from collections import deque
def process_input(path):
    equations = dict()
    with open(path, 'r') as file:
        for line in file:
            target, rest = line.split(':')
            operands = deque(map(int, rest.strip().split(' ')))
            equations[int(target)] = operands
    return equations

def can_solve(target, operators, operands):
    if len(operands) == 1:
        return operands[0] == target
    
    a = operands.pop()
    a_len = len(str(a))

    for op in operators:
        if op == '+' and target - a > 0:
            new_target = target - a
        elif op == '*' and target % a == 0:
            new_target = target // a
        elif op == '|' and (target - a) % 10 ** (a_len) == 0:
            removed = str(target)[:-a_len]
            new_target = int(removed) if removed else 0 
        else:
            continue
        if can_solve(new_target, operators, operands):
            return True 
    operands.append(a)
    return False

def count_solvable(equations, operators):
    total = 0
    for target, operands in equations.items():
        if can_solve(target, operators, operands):
            total += target
    return total


if __name__ == "__main__":
    equations = process_input('full_input.txt')
    print(f"solvable with *+: {count_solvable(equations, '*+')}")
    print(f"solvable with *+|: {count_solvable(equations, '*+|')}")