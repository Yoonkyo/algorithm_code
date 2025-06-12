class Solution:
    def maxDfromAtoB(self, a: int, b: int, k: int, n: int, freq: List[List[int]]) -> int:
        INF = 10**8
        cnt = float('-inf')
        minDiff = [[INF] * 2 for _ in range(2)]
        l = 0

        for r in range(k - 1, n):
            freqA = freq[a][r + 1]
            freqB = freq[b][r + 1]

            while r - l + 1 >= k and freqB - freq[b][l] >= 2:
                preA = freq[a][l]
                preB = freq[b][l]
                minDiff[preA & 1][preB & 1] = min(minDiff[preA & 1][preB & 1], preA - preB)
                l += 1

            cnt = max(cnt, freqA - freqB - minDiff[1 - (freqA & 1)][freqB & 1])
        return cnt

    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        freq = [[0] * (n + 1) for _ in range(5)]

        for i in range(n):
            digit = int(s[i])
            for d in range(5):
                freq[d][i + 1] = freq[d][i]
            freq[digit][i + 1] += 1

        ans = float('-inf')
        for a in range(5):
            if freq[a][n] == 0:
                continue
            for b in range(5):
                if a != b and freq[b][n] > 0:
                    ans = max(ans, self.maxDfromAtoB(a, b, k, n, freq))
        return ans
