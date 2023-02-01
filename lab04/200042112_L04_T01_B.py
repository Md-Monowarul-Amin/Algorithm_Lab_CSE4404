def dfs(start_node , adj_matrix, visited_list):
    for i in range(len(adj_matrix[start_node])):
        if adj_matrix[start_node][i] == 1 and visited_list[i] != 1:
            visited_list[i] = 1
            dfs(i, adj_matrix, visited_list)

    return


n, m = map(int, input().split())
adj_matrix = []

for i in range(n+1):
    temp_matrix = []
    for j in range(n+1):
        temp_matrix.append(0)
    adj_matrix.append(temp_matrix)

for i in range(m):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1


start_check_list = list(map(int, input().split()))
visited = []
for j in range(n+1):
    visited.append(0)
#print(adj_matrix)
#print(start_check_list)
for i in range(start_check_list[0]):
    for j in range(n):
        visited[j] = 0

    start_node = start_check_list[i+1]
    dfs(start_node, adj_matrix, visited)
    # print(start_node, visited)
    print(len(visited)- sum(visited) - 1, end=" ")
    for j in range(1, len(visited)):
        if visited[j] == 0:
            print(j, end=" ")
    print()



