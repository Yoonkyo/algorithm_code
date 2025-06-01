class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if 3 * limit < n:
            return 0
        if limit >= n:
            return (n + 2) * (n + 1) // 2 
        count = 0
        for i in range(max(0, n - 2 * limit), min(limit, n) + 1):
            min_j = max(0, n - i - limit)
            max_j = min(limit, n - i)
            count += max_j - min_j + 1
        return count
