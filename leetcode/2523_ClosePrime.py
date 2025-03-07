class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right+1)
        for num in range(2, int(right**0.5) + 1):
            if is_prime[num]:
                for composite in range(num**2, right + 1, num):
                    is_prime[composite] = False
        if left == 1:
            left += 1
        prime_list = [p for p in range(left, right + 1) if is_prime[p]]
        if len(prime_list) < 2:
            return [-1,-1]
        gap_min = right-left+1
        for i in range(len(prime_list)-1):
            gap = prime_list[i+1] - prime_list[i]
            if gap < gap_min:
                gap_min = gap
                pair = [prime_list[i], prime_list[i+1]]
        return pair