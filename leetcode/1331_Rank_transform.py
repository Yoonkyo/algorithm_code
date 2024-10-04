class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if arr == []:
            return []
        ranks = [0]*len(arr)
        result = [0]*len(arr)
        a = sorted(arr)
        rank = 1
        prev = a[0]
        for i in range(len(arr)):
            if a[i] > prev:
                rank += 1
                prev = a[i]
            ranks[i] = rank
        dic = dict(zip(a, ranks))
        for i in range(len(arr)):
            result[i] = dic[arr[i]]
        return result
