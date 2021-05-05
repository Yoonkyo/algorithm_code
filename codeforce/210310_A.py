def solution(count):
    for counting in range(count):
        integer_list = input().split(" ")
        integer_list = list(map(int, integer_list))
        n = integer_list[0]
        k = integer_list[1]
        string = input()
        result = "NO"
        weight = 0
        if k == 0:
            print("YES")
            continue
        if n%2 == 1:
            if n//2 < k:
                print("No")
                continue
            while (n//2 - weight) >= k:
                if string[0:n//2 - weight] == string[n-1:n//2+weight:-1]:
                    result = "YES"
                    break
                weight += 1
            print(result)
        else:
            if n//2 <= k:
                print("No")
                continue
            while (n//2 - weight) > k:
                if string[0:n//2-1-weight] == string[n-1:n//2+weight:-1]:
                    result = "YES"
                    break
                weight += 1
            print(result)

a = int(input())
solution(a)