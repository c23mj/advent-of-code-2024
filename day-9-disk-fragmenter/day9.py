def process_input(path):
    disk = []
    order = []
    disks = dict()

    with open(path, 'r') as file:
        line = file.readline().strip()
        n = len(line)
        for i in range(n):
            count = int(line[i])
            if i % 2 == 0:
                curr_id = i // 2
                disks[curr_id] = (len(disk), len(disk) + count - 1)
                disk.extend([curr_id] * count)
                order.extend([curr_id] * count)
            else:
                disk.extend(['.'] * count)

    return disk, order, disks

def move_partial(disk, order):
    n = len(order)
    i, j = 0, n - 1
    moved = []
    for k in range(n):
        if isinstance(disk[k], int):
            moved.append(order[i])
            i += 1
        else:
            moved.append(order[j])
            j -= 1
    return moved

def get_disk_state(disks, order):
    res = []
    last_end = float('inf')
    for val in order:
        disk_start, disk_end = disks[val]
        curr_disk_size, curr_free_size = disk_end - disk_start + 1, disk_start - last_end - 1
        if curr_free_size > 0:
            res.extend(['.'] * curr_free_size)
        res.extend([val] * curr_disk_size)
        last_end = disk_end
    return res


def move_fully(disks):

    n = len(disks)
    # print(disks)

    order = list(range(n))
    for i in range(n-1, -1, -1):
   
        curr_disk = disks[i]
        disk_size = curr_disk[1] - curr_disk[0] + 1
        # print(f"to insert: {i}. disk size: {disk_size}")
       
        last_end = float('inf')
        for j in range(n):
            curr_start, curr_end = disks[order[j]]
            if curr_start > curr_disk[0]:
                break

            # print(f"trying to insert before disk {order[j]}")
            # print(f"start of this disk: {curr_start}. end of last disk: {last_end}")
            if curr_start - last_end - 1 >= disk_size:
                # print(f"inserting.")
                disks[i] = (last_end + 1, last_end + disk_size)
                # print(f"new disks[{i}]: {disks[i]}")
                order.remove(i) 
                order.insert(j, i)
                # print(f"new order: {order}")
                break
            last_end = curr_end
    return get_disk_state(disks, order)
    
                    
def move_and_calc_checksum(disk, order, disks, partial=True):
    if partial:
        moved = move_partial(disk, order)
    else:
        moved = move_fully(disks)
    return sum(pos * id if isinstance(id, int) else 0 for pos, id in enumerate(moved) )


if __name__ == "__main__":
    disk, order, disks = process_input('full_input.txt')
    print(move_and_calc_checksum(disk, order, disks))
    print(move_and_calc_checksum(disk, order, disks, False))

    