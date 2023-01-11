def check(grid, visited, found_island, i, j):
    if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i])-1:
            return 0

    if grid[i][j+1] == 0 and visited[i][j+1] == 0:
        visited[i][j+1] += 1
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i])-1:
            return 0
        else:
            check(grid, visited, found_island, i, j+1)

    
    if grid[i+1][j] == 0 and visited[i+1][j] <= found_island:
        visited[i+1][j] += 1
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i]) - 1:
            return 0
        else:
            check(grid, visited, found_island, i+1, j)

    if grid[i][j-1] == 0 and visited[i][j-1] == 0:
        visited[i][j-1] += 1
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i])-1:
            return 0
        else:
            check(grid, visited, found_island, i, j-1)

    if grid[i-1][j] == 0 and visited[i-1][j] == 0:
        visited[i-1][j] += 1
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i])-1:
            return 0
        else:
            check(grid, visited, found_island, i-1, j)
    else:
        return 1

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
visited = []
zero_count_in_grid = 0
        
for i in range(len(grid)):
    temp_list = []
    for j in range(len(grid[i])):
        temp_list.append(0)
        if grid[i][j] == 0:
            zero_count_in_grid += 1
    visited.append(temp_list)


found_island = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        #print(grid[row][col], end=" ")
        if grid[row][col] == 0 and visited[row][col] == 0:
            visited[row][col] = 1
            # print(row, col)
            found = check(grid, visited, found_island, row, col)
            found_island += found
            #print(found_island)

    #print()
# print(zero_count_in_grid)
print(found_island)
