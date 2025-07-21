class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count = 1
            if count < 3:
                result += s[i-1]
        result += s[-1]
        return result
