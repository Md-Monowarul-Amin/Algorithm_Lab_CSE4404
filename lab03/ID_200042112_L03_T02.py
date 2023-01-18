###Problem Link
"""https://leetcode.com/problems/n-ary-tree-level-order-traversal/"""

root = list(map(str, input().split()))
output = 0
for i in range(len(root)):
    left_ind_i = (i+1) * 2 - 1
    if left_ind_i < len(root):
        if root[left_ind_i] == "null":
            pass
        else:
            output += int(root[left_ind_i])

print(output)


"""
3 9 20 null null 15 7
"""
