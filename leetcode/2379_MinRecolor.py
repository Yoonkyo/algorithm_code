class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        oper = 0
        min_oper = k
        for i in range(len(blocks)-k+1):
            oper = blocks[i:i+k].count("W")
            if oper == 0:
                return 0
            elif min_oper > oper:
                min_oper = oper
            oper = 0
        return min_oper