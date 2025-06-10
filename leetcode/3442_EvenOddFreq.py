class Solution:
    def maxDifference(self, s: str) -> int:
        alpha_dict = {}
        odd = 1
        even = 100 
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for alpha in alphabet:
            alpha_dict[alpha] = 0
        for i in s:
            alpha_dict[i] += 1
        for j in alphabet:
            count = alpha_dict[j]
            if count == 0:
                continue
            if count%2 == 1 and count > odd:
                odd = count
            elif count%2 == 0 and count < even:
                even = count
        return odd-even
