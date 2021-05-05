def solution(count):
    for counting in range(count):
        limit_list = input().split(" ")
        limit_list = list(map(int, limit_list))
        h = limit_list[0]
        m = limit_list[1]

        time = input()
        hour = int(time[0:2])
        min = int(time[3:])

        # print(hour)
        while(hour < h):
            if hour < 10:
                time = '0' + str(hour) + time[2:]
            else:
                time = str(hour) + time[2:]
            while (min < m):
                if min < 10:
                    time = time[0:4] + str(min)
                else:
                    time = time[0:3] + str(min)
                new = digit_dic[time[4]] + digit_dic[time[3]]+ ':'+ digit_dic[time[1]]+ digit_dic[time[0]]
                if 'x' not in new and int(new[0:2]) < h and int(new[3:]) < m:
                    print(time)
                    break
                else:
                    min += 1
            if 'x' not in new and int(new[0:2]) < h and int(new[3:]) < m:
                break
            hour += 1
            min = 0
            time = time[0:3] + '00'
        if 'x' in new:
            print("00:00")


digit_dic = {'0':'0', '1':'1', '2':'5', '3':'x', '4':'x', '5':'2', '6':'x', '7':'x', '8':'8', '9':'x'}
a = int(input())
solution(a)