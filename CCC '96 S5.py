from sys import *
n = int(stdin.readline())
lst_all = []
for th in range(n):
    lst_of_diff = []
    length = int(stdin.readline())
    lst_1 = list(map(int, stdin.readline().split()))
    lst_2 = list(map(int, stdin.readline().split()))
    lst_2.reverse()
    position = 0
    while position < length:
        element = lst_1[position]
        for hj in range(length):
            if lst_2[hj] >= element:
                if length-1-hj > position:
                    lst_of_diff.append(length-1-hj-position)
                else:
                    lst_of_diff.append(0)
        position = position + lst_1.count(element)
    lst_all.append(max(lst_of_diff))
for j in range(n):
    print("The maximum distance is", lst_all[j])