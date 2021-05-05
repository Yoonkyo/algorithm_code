def solution(count):
    for counting in range(count):
        integer_list = input().split(" ")
        integer_list = list(map(int, integer_list))
        n = integer_list[0]
        k = integer_list[1]
        string = input()

        if n % k != 0:
            print(-1)
            continue
        
        answer = ''
        while (answer != True):
            for i in reversed(range(len(string))

        for i in range(ord('a'), ord('z') + 1):
        print(chr(i))

        print('print =', string)



a = int(input())
solution(a)