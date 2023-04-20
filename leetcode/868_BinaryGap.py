class Solution:
    def binaryGap(self, n: int) -> int:
        binary = str(bin(n)[2:])
        long_d = 0
        d = 0
        for i in binary:
            if i != '1':
                d += 1            
            else:
                long_d = max(long_d, d)
                d = 1
        return long_d
