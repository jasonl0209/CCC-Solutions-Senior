from sys import *
n = int(stdin.readline())
lst_time = []
lst_distance = []
lst_speeds = []
for j in range(n):
    time, distance = map(int, stdin.readline().split())
    lst_time.append(time)
    lst_distance.append(distance)
lst_time_sorted = sorted(lst_time)
new_list_distance = [lst_distance[lst_time.index(lst_time_sorted[0])]]
max_speed = 0
lower_index = lst_distance[lst_time.index(lst_time_sorted[0])]
for i in range(1, n):
    upper_index = lst_distance[lst_time.index(lst_time_sorted[i])]
    speed = abs((upper_index - lower_index) / (lst_time_sorted[i] - lst_time_sorted[i-1]))
    if speed > max_speed:
        max_speed = speed
    lower_index = upper_index
print(max_speed)
