def search(adj_list:list, visited, i):
    # print((i, "i"))
    visited[i] = 1
    for k in range(len(adj_list[i])):
        if visited[k] == 0 and adj_list[i][k] == 1:
            visited[k] = 1
            search(adj_list, visited, k)


n = int(input())
int_list_2d = []
visited = []
for i in range(n):
    visited.append(0)

for i in range(n):
    int_list = list(map(int, input().split()))
    int_list_2d.append(int_list)

province_count = 0
for i in range(n):
    if visited[i] == 0:
        province_count += 1
        search(int_list_2d, visited, i)

print(province_count)


"""10
1 1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0
1 1 1 1 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 0 0 1 1 1 1 0 0 
0 0 0 0 1 1 1 0 0 0
0 0 0 0 0 1 0 1 0 0
0 0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0 1 1
"""