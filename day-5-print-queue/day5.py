from collections import defaultdict
def process_input(path):
    rules = defaultdict(set)
    printers = []
    input_is_rules = True
    with open(path, 'r') as file:
        for line in file:
            if line == '\n':
                input_is_rules = False
                continue
            if input_is_rules:
                before, after = map(int, line.strip().split('|'))
                rules[after].add(before)
            else:
                printers.append(list(map(int, line.strip().split(','))))
    return rules, printers

def count_valid(rules, printers):
    def get_sum(printer):
        seen = set()
        for page in printer:
            if seen - rules[page]:
                return 0
            seen.add(page)
        middle =  printer[len(printer) // 2]
        return middle
    
    middle_sum = 0
    for printer in printers:
        middle_sum += get_sum(printer)
        
    return middle_sum

from collections import deque
def count_invalid(rules, printers):
    def topo_middle_sum(pages):
        n = len(pages)
        in_degree = {page: 0 for page in pages}
        for u, successors in rules.items():
            if u not in pages:
                continue
            for v in successors:
                if v in pages:
                    in_degree[v] += 1

        correct_order = sorted(list(pages), key = lambda x: in_degree[x])       
        return correct_order[n // 2]
        
    def get_sum(printer):
        seen = set()
        for page in printer:
            if seen - rules[page]:
                return topo_middle_sum(set(printer))
            seen.add(page)
        return 0
    
    middle_sum = 0
    for printer in printers:
        middle_sum += get_sum(printer)
        
    return middle_sum

    

if __name__ == "__main__":
    rules, printers = process_input('full_input.txt')
    print(f"valid printer middle sum: {count_valid(rules, printers)}")
    print(f"(corrected) invalid printer middle sum: {count_invalid(rules, printers)}")

