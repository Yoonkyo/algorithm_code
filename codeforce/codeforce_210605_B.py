import math

def solution(t):
    for counting in range(t):
        result = 0
        length = int(input())
        integer_list = input().split(" ")
        integer_list = list(map(int, integer_list))
        new_list = []
        for integer in integer_list:
            if integer % 2 == 1:
                new_list.append(integer)
            else:
                new_list = [integer] + new_list
        for i in range(length):
            k = i+1
            for j in range(k, length):
                x = new_list[i]
                y = new_list[j]
                if math.gcd(x, 2*y) > 1:
                    result += 1
        print(result)

a = int(input())
solution(a)