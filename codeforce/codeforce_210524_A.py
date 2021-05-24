def solution(t):
    for counting in range(t):
        length = int(input())
        integer_list = input().split(" ")
        integer_list = list(map(int, integer_list))
        min_value = min(integer_list)
        result = 0
        for i in integer_list:
            if min_value < i:
                result += 1
        print(result)
a = int(input())
solution(a)