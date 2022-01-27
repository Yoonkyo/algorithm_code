class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        list_1 = []
        list_2 = []
        result = []
        for i in nums:
            if i > 0:
                list_1.append(i)
            else:
                list_2.append(i)
        for i in range(len(list_1)):
            result.append(list_1[i])
            result.append(list_2[i])
        return result
