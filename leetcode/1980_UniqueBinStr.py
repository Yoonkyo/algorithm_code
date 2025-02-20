class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        num_set = set(nums)  # Convert the list to a set for O(1) lookups
        
        # Generate all possible binary strings of length n
        for i in range(2 ** n):
            candidate = format(i,'b').zfill(n)  # Convert to binary and pad with leading zeros
            if candidate not in num_set:
                return candidate
