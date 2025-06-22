class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        group_num = len(s)//k
        if len(s)%k > 0:
            group_num += 1
        group = [""]*group_num
        for i in range(group_num):
            group[i] = s[i*k:i*k+k]    
        if len(s)%k > 0:
            group[-1] += fill*(k-len(s)%k)
        return group
