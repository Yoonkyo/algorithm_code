def solution(t):
    for counting in range(t):
        integer_list = input().split(" ")
        integer_list = list(map(int, integer_list))
        r = integer_list[0]
        b = integer_list[1]
        d = integer_list[2]

        if r == b:
            print("YES")
        if d == 0:
            if r != b:
                print("NO")
        else:
            if r > b: 
                max = r
                min = b
            else:
                max = b
                min = r
            if max/min - 1 <= d:
                print("YES")
            else:
                print("NO")

a = int(input())
solution(a)