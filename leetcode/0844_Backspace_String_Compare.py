class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def edit(string):
            new_s = ""
            for i in string:
                if i == "#":
                    new_s = new_s[0:-1]
                else:
                    new_s += i
            return new_s
        if edit(s) == edit(t):
            return True
        else:
            return False
