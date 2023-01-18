###Problem Link
"""https://leetcode.com/problems/course-schedule-ii/"""
def dfs(adj_list, out_list: list, visited, start):
    visited[start] = 1
    out_list.append(start)
    for i in range(len(adj_list)):
        if adj_list[start][i] == 1 and visited[i] == 0:
            dfs(adj_list, out_list, visited, i)


numCources = int(input())
prerequisites = []
for i in range(numCources):
    temp_list = list(map(int, input().split()))
    prerequisites.append(temp_list)

adj_list = []
for i in range(numCources):
    temp_list = []
    for j in range(numCources):
        temp_list.append(0)
    adj_list.append(temp_list)
    temp_list = []

####Create Graph
for pre_req in range(numCources):
    adj_list[prerequisites[pre_req][1]][prerequisites[pre_req][0]] = 1

# print(adj_list)

indegrees = []
for i in range(numCources):
    indegrees.append(0)

###Check Indegrees
for pre_req in range(numCources):
    for i in range(numCources):
        if adj_list[pre_req][i] == 1:
            indegrees[i] += 1

# print(indegrees)

visited = []
out_list = []
for i in range(numCources):
    visited.append(0)

for i in range(len(indegrees)):
    if indegrees[i] == 0:
        dfs(adj_list, out_list, visited, indegrees[i])

while sum(indegrees) != numCources:
    for i in range(len(visited)):
        if visited[i] == 0:
            dfs(adj_list, out_list, visited, indegrees[i])

print(out_list)

"""
4
1 0
2 0
3 1
3 2
"""
