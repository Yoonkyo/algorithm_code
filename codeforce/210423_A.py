def solution(t):
    for counting in range(t):
        number = int(input())
        count = 1
        if number < 2050:
            print(-1)
            continue
        while number >= 2050:
            length = digit_length(number)
            number_2050 = 2050*10**(length - 4)
            if number == number_2050:
                break
            if number >= number_2050:
                number -= number_2050
            elif number_2050/10 < 2050:
                count = -1
                break
            else:
                number -= number_2050/10
            count += 1
            if number < 2050:
                count = -1
        print(count)

def digit_length(n):
    ans = 0
    while n:
        n //= 10
        ans += 1
    return ans

a = int(input())
solution(a)