dp = []
def find_shortest(current_i, current_j, maze, total_row, total_col, from_i, from_j, min_list):
    global dp
    
    if current_i >= total_row or current_i < 0 or current_j < 0 or current_j >= total_col:
        return 10 ** 8
    
    if current_i +1 == total_row and current_j +1 == total_col:  
        # min_list.append(maze[current_i][current_j])
        dp[current_i][current_j] = maze[current_i][current_j] 
        return maze[current_i][current_j] 

    if dp[current_i][current_j] != -1:
        return dp[current_i][current_j]
    # if  current_j + 1 == total_col and current_i + 1 == total_row - 1:
    #     # min_list.append(maze[current_i][current_j])
    #     return maze[current_i][current_j]
    
    if current_i + 1 == from_i and current_j == from_j:
        dp[current_i][current_j] = maze[current_i][current_j] + min(
                                                 find_shortest(current_i - 1, current_j, maze, total_row, total_col, current_i, current_j, min_list), 
                                                 find_shortest(current_i, current_j + 1, maze, total_row, total_col, current_i, current_j, min_list), 
                                                 find_shortest(current_i, current_j - 1, maze, total_row, total_col, current_i, current_j, min_list))
        return dp[current_i][current_j]

    if current_i - 1 == from_i and current_j == from_j:
        dp[current_i][current_j] = maze[current_i][current_j] + min(find_shortest(current_i + 1, current_j, maze, total_row, total_col, current_i, current_j, min_list),
                                                 find_shortest(current_i, current_j + 1, maze, total_row, total_col, current_i, current_j, min_list), 
                                                 find_shortest(current_i, current_j - 1, maze, total_row, total_col, current_i, current_j, min_list))
        return dp[current_i][current_j]

    if current_i == from_i and current_j + 1== from_j:
        dp[current_i][current_j] = maze[current_i][current_j] + min(find_shortest(current_i + 1, current_j, maze, total_row, total_col, current_i, current_j, min_list),
                                                 find_shortest(current_i - 1, current_j, maze, total_row, total_col, current_i, current_j, min_list), 
                                                 find_shortest(current_i, current_j - 1, maze, total_row, total_col, current_i, current_j, min_list))

        return dp[current_i][current_j]

    if current_i == from_i and current_j - 1 == from_j:
        dp[current_i][current_j] = maze[current_i][current_j] + min(find_shortest(current_i + 1, current_j, maze, total_row, total_col, current_i, current_j, min_list),
                                                 find_shortest(current_i - 1, current_j, maze, total_row, total_col, current_i, current_j, min_list), 
                                                 find_shortest(current_i, current_j + 1, maze, total_row, total_col, current_i, current_j, min_list))
        return dp[current_i][current_j]

    # return 10 ** 8
    # if 0 <= current_i + 1 < total_row and from_i != current_i + 1:
    #     print(current_i, current_j, maze[current_i][current_j])
    #     return(maze[current_i][current_j] + find_shortest(current_i + 1, current_j, maze, total_row, total_col, current_i, current_j, min_list))
        
    # if 0<=current_i -1 < total_row and from_i != current_i - 1:
    #     return(maze[current_i][current_j] + find_shortest(current_i - 1, current_j, maze, total_row, total_col, current_i, current_j, min_list))


    # if 0 <= current_j +1 < total_col and from_j != current_j + 1:
    #     return(maze[current_i][current_j] + find_shortest(current_i, current_j + 1, maze, total_row, total_col, current_i, current_j, min_list))

    # if 0 <= current_j - 1 < total_col and from_j != current_j - 1:
    #     return(maze[current_i][current_j] + find_shortest(current_i, current_j - 1, maze, total_row, total_col, current_i, current_j, min_list))

    # else:
    #     # min_list.append(10 ** 8)
    #     return 10 ** 8

n, m = map(int, input().split())
maze = []
for i in range(n):
    temp_maze = list(map(int, input().split()))
    maze.append(temp_maze)
min_list = []
#print(maze, len(maze), len(maze[0]))

for i in range(n + 1):
    temp_dp = []
    for j in range(m +1):
        temp_dp.append(-1)
    dp.append(temp_dp)


# print(dp)
if m > 1 and n > 1:
    print(find_shortest(0, 1, maze, len(maze), len(maze[0]), 0, 0, min_list))
    print(find_shortest(1, 0, maze, len(maze), len(maze[0]), 0, 0, min_list))

elif n > 1:
    print(find_shortest(1, 0, maze, len(maze), len(maze[0]), 0, 0, min_list))

elif m > 1:
    print(find_shortest(0, 1, maze, len(maze), len(maze[0]), 0, 0, min_list))

# print(min(min_list))
print(dp)
print(maze)

