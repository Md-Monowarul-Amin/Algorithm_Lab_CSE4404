n = int(input())
int_list_2d = []
for i in range(n):
    int_list = list(map(int, input().split()))
    # print(int_list)
    int_list_2d.append(int_list)

found = 0
for col in range(n):
    ok = 1
    for row in range(n):
        if int_list_2d[row][col] == 0:
            ok = 0
            break

    if ok:
        found = 1
        print("Person " + str(col) + " is a celebrity.")
        break

if not found:
    print("There is no celebrity.")


