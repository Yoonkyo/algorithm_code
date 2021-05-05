def solution(count):
    for counting in range(count):
        integer_list = input().split(" ")
        integer_list = list(map(int, integer_list))
        answer_list = []
        n = integer_list[0]
        k = integer_list[1]
        for i in range(k,n):
            now = i+1
            answer_list.append(now)
        if n == 1:
            print('0')
            continue    
        elif k%2 == 0:
            for j in range(k//2, k):
                answer_list.append(j)
        else:
            for j in range(k//2+1, k):
                answer_list.append(j)
        print(len(answer_list))
        answer = ''
        for i in answer_list:
            answer = answer + str(i) + ' '
        print(answer)

a = int(input())
solution(a)