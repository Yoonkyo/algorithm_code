def solution(t):
    for counting in range(t):
        integer_list = input().split(" ")
        integer_list = list(map(int, integer_list))
        max_1 = max(integer_list[0:2])
        max_2 = max(integer_list[2:])
        total_max = max(integer_list)
        integer_list.remove(total_max)
        total_max_2nd = max(integer_list)
        if total_max == max(max_1, max_2) and total_max_2nd == min(max_1, max_2):
            print("YES")
        else:
            print("NO")
a = int(input())
solution(a)