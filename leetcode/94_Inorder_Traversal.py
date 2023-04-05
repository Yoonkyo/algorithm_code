# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inorder(values, node):
            if node:
                inorder(values,node.left)
                result.append(node.val)
                inorder(values,node.right)
            return values
        return inorder(result, root)
