import math

def solution(count):
    for counting in range(count):
        integer_list = input().split(" ")
        integer_list = list(map(int, integer_list))
        n = integer_list[0]
        k = integer_list[1]
        testcase_list = input().split(" ")
        testcase_list = list(map(int, testcase_list))

        for i in range(k):
            start = 0
            while start < n:
                if start != testcase_list[start]:
                    a = start
                    break
                start += 1
                if start == n:
                    a = start
                    break
            b = max(testcase_list)
            result = math.ceil((a+b)/2)
            if result not in testcase_list:
                testcase_list.append(result)
            n = len(testcase_list)
        print(len(testcase_list))
#        new_list = []   
#        for v in testcase_list:
#            if v not in new_list:
#                new_list.append(v)
#        print(len(new_list))

a = int(input())
solution(a)