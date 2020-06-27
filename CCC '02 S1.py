import sys
input = sys.stdin.radline()
pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
raised = int(input())
counter = 0
lst = []
lst2 = []
for i in range((raised//pink)+1):
    for k in range((raised//green)+1):
        for y in range((raised//red)+1):
            for d in range((raised//orange)+1):
                if i*pink+k*green+y*red+d*orange == raised:
                    counter+=1
                    lst.append(i)
                    lst.append(k)
                    lst.append(y)
                    lst.append(d)
for o in range(len(lst)//4):
    print("# of PINK is", lst[0], "# of GREEN is", lst[1], "# of RED is", lst[2], "# of ORANGE is", lst[3])
    lst2.append(lst[0]+lst[1]+lst[2]+lst[3])
    lst = lst[4:]
print("Total combinations is", str(counter)+".")
print("Minimum number of tickets to print is", str(min(lst2))+".")
