# 1A - Theatre Square
def solution(input_list):
    n = input_list[0]
    m = input_list[1]
    a = input_list[2]
    if n%a != 0:
        i = n//a+1
    else:
        i = n//a
    if m%a != 0:
        j = m//a+1
    else:
        j = m//a
    print(i*j)

info_list = input().split(" ")
info_list = list(map(int, info_list))
solution(info_list)