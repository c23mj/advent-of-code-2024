def process_input(path):
    left_list, right_list = [], []
    with open(path, 'r') as file:
        for line in file:
            left_item, right_item = map(int, line.split())
            left_list.append(left_item)
            right_list.append(right_item)
    return left_list, right_list

def get_list_distance(left_list, right_list):
    n = len(left_list) 
    left_list.sort()
    right_list.sort()
    return sum(abs(left_list[i] - right_list[i]) for i in range(n))

from collections import Counter
def get_list_similarity_score(left_list, right_list):
    left_counter, right_counter = Counter(left_list), Counter(right_list)
    total_score = 0
    for key, left_count in left_counter.items():
        total_score += key * left_count * right_counter[key]
    
    return total_score



if __name__ == "__main__":
    left_list, right_list = process_input('full_input.txt')
    print(f"list distance: {get_list_distance(left_list, right_list)}")
    print(f"list similarity score: {get_list_similarity_score(left_list, right_list)}")