lst = []
inp_getter = [1, 2]
lst_temp = []
while inp_getter[0] != "Waterloo":
    inp_getter = input().split(" ")
    lst.append(inp_getter[0])
    lst.append(int(inp_getter[1]))
    lst_temp.append(int(inp_getter[1]))
print(lst[lst.index(min(lst_temp)) - 1])
