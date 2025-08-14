class Solution:
    def largestGoodInteger(self, num: str) -> str:
        check = 0
        prev = ""
        result = ""
        for i in num:
            if i == prev:
                check += 1
            else:
                check = 0
            if check >= 2 and i*3 > result:
                result = i*3
            prev = i
        return result
