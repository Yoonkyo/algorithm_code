# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def generator(nums):
            if len(nums) == 0:
                return None
            top_node = nums[len(nums) // 2]
            root = TreeNode(top_node)
            root.left = generator(nums[:len(nums) // 2])
            root.right = generator(nums[len(nums) // 2 + 1:])
            return root
        return generator(nums)
