class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def signature(x: int):
            cnt = [0]*10
            while x:
                cnt[x % 10] += 1
                x //= 10
            return tuple(cnt)

        target = signature(n)
        for k in range(31):  # 0..30
            if signature(1 << k) == target:
                return True
        return False
