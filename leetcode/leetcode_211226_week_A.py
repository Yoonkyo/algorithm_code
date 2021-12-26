class Solution(object):
    def isSameAfterReversals(self, num):
        if num == 0:
            return True
        result = ""
        reverse_num = str(num)[::-1]
        for i in reverse_num:
            result += i
            if result == "0":
                return False
        return True
        
        """
        :type num: int
        :rtype: bool
        """
