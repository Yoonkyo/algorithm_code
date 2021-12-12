class Solution(object):
    def countPoints(self, rings):
        length = len(rings)//2
        check = []
        for i in range(10): 
            check += [[0,0,0]]
        result = 0
        for i in range(length):
            color = rings[2*i]
            loc = int(rings[2*i+1])
            if color == 'R':
                check[loc][0] = 1
            elif color == 'G':
                check[loc][1] = 1
            elif color == 'B':
                check[loc][2] = 1
        
        for ring_check in check:
            if 0 not in ring_check:
                result += 1
        return result
        """
        :type rings: str
        :rtype: int
        """
