class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        result1 = []
        result2 = []

        for i in nums1_set:
            if i not in nums2_set:
                result1.append(i)
            else:
                nums2_set.remove(i)
        result2 = list(nums2_set)

        return [result1, result2]
