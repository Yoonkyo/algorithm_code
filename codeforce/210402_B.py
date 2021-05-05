def solution(count):
    for counting in range(count):
        length = int(input())
        string_a = input()
        string_b = input()
        count_a = 0
        count_b = 0
        result = "YES"
        # Check 1
        count_a = string_a.count('1')
        count_b = string_b.count('1')
        if count_a%2 != count_b%2:
            print("NO")
            continue
        if length %2 == 1:
            prefix = length - 1
            if string_a[prefix] != string_b[prefix]:
                print("NO")
                continue
        else:
            prefix = length

        # Check 2
        while(prefix >= 0):
            check_a = string_a[prefix-2:prefix]
            check_b = string_b[prefix-2:prefix]
            if check_a == check_b:
                prefix -= 2
                continue
            elif check_a.count('1')%2 != check_b.count('1')%2:
                result = "NO"
                break
            elif string_a[0:prefix].count('1') != prefix// 2:
                result = "NO"
                break
            else:
                string_a = string_a[0:prefix]
                string_a = string_a.replace('1', 'a')
                string_a = string_a.replace('0', '1') 
                string_a = string_a.replace('a', '0') 
                prefix -= 2
                continue
        print(result)
        
a = int(input())
solution(a)