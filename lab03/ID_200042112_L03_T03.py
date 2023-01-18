###Problem Link
"""https://leetcode.com/problems/n-ary-tree-level-order-traversal/"""
root = list(map(str, input().split()))
node_dict = dict()
curr_node = 1

highest_node_val = int(root[len(root)-1])
for i in range(1, highest_node_val+1):
    node_dict[i] = []

if len(root) >= 3:
    for i in range(2, len(root)):
        if root[i] == "null":
            curr_node += 1
        else:
            node_dict[curr_node].append(root[i])

print(node_dict)

out_list = [[1]]
appended_in_out_list = 1
while appended_in_out_list < highest_node_val:
    temp_list = []
    for i in range(len(out_list[-1])):
        num = out_list[-1][i]
        print(num, out_list)
        if len(node_dict[int(num)]) > 0:
            for j in range(len(node_dict[int(num)])):
                temp_list.append(node_dict[int(num)][j])
                appended_in_out_list += 1
    out_list.append(temp_list)


print(out_list)


"""
1 null 2 3 4 5 null null 6 7 null 8 null 9 10 null null 11 null 12 null 13 null null 14
"""