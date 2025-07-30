class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        result = ""
        for i in s_list:
            result += i[::-1]
            result += " "
        return result[:-1]
