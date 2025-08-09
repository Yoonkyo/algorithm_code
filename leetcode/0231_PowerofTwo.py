class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        check = list(str(bin(n)[2:]))
        check.remove('1')
        if '1' in check:
            return False
        else:
            return True
