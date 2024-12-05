def process_input(path):
    lists = []
    with open(path, 'r') as file:
        for line in file:
            lists.append(list(map(int, line.split())))
    return lists

# brute force but eh the lists are small enough and i'm not thinking of something smarter
def is_safe_with_tol(list):
    for i in range(len(list)):
        if is_safe(list[:i] + list[i+1:]):
            return True
    return False
    
def is_safe(list):
    if len(list) - len(set(list)) > 0:
       return False
    decr, incr = False, False
    for i in range(1, len(list)):
        diff = list[i] - list[i - 1]
        if 1 <= diff <= 3 and not decr:
            incr = True
        elif -3 <= diff <= -1 and not incr:
            decr = True
        else:
            return False
            
    return True

    
def count_safe(lists, tol=False):
    total_safe = 0
    for list in lists:
        if is_safe(list) or (tol and is_safe_with_tol(list)):
            total_safe += 1
    return total_safe


if __name__ == "__main__":
    lists = process_input('full_input.txt')
    print(f"There are a total of {count_safe(lists)} safe lists.")
    print(f"There are a total of {count_safe(lists, 1)} tolerantly-safe lists.")