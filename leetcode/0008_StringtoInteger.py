class Solution:
    def myAtoi(self, s: str) -> int:
        def stoi(s):
            result = '0'
            digits = [str(i) for i in range(10)]
            for word in s:
                if word in digits:
                    result += word
                else:
                    break
            return int(result)

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        neg = 1
        s=s.strip()
        if not s:
            return 0
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                neg = -1
            s = s[1:]
        elif s[0] not in digits:
            return 0

        answer = stoi(s)*neg
        if answer > INT_MAX:
            answer = INT_MAX
        elif answer < INT_MIN:
            answer = INT_MIN
        return answer
