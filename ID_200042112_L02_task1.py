def move(start, end):
    level = 0
    if start == end:
        return level
    

    dx = [2, 2, -2, -2, 1, 1,-1, -1 ]
    dy = [1, -1, 1, -1, 2,-2, 2, -2]
    start = int(start)
    end = int(end)
    queue = []
    queue.append(start)
    level_dict = dict()
    level_dict[start] = 0
    while len(queue) != 0:
        curr_cell = queue[0]
        # print(curr_cell, "current cell")
        # print(level_dict)
        queue.pop(0)
        level += 1
        for i in range(8):
            cell_num = curr_cell + dx[i] * 10 + dy[i]

            if 10 < cell_num < 89 and  0 < cell_num % 10 <= 8:
                queue.append(cell_num)
                if (cell_num) not in level_dict:
                    level_dict[(cell_num)] = level_dict[curr_cell] + 1
                else:
                    level_dict[(cell_num)] = min(level_dict[cell_num], level_dict[curr_cell] + 1)
  
                if cell_num == end:
                    print(level_dict)
                    return level_dict[(cell_num)]
    
    
    return 0

start, end = map(str, input().split())

start_modified = str(ord(start[0])-96) + str(start[1])
end_modified = str(ord(end[0])-96) + str(end[1])
# print(start_modified, end_modified)
print(move(start_modified, end_modified))
#print(move(start, end, 0))
