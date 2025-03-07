class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        new_list = []
        for l in grid:
            new_list += l
        new_list.sort()
        check = 1
        a, b = 0, 0
        for i in range(len(new_list)):
            if check != new_list[i]:
                if check-1 == new_list[i]:
                    check -= 1
                    a = check
                else:
                    b = check
                    check += 1
            check += 1
        if b == 0:
            b = len(new_list)
        return [a,b]