def arena(n):
    for i in range(n):
        heroes = int(input())
        level_list = input().split(" ")
        min_level = min(level_list)
        while min_level in level_list:
            level_list.remove(min_level)
        print(len(level_list))

a = int(input())
arena(a)