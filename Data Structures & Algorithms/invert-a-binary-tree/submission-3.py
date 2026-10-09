# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        new_R = self.invertTree(root.left)
        new_L = self.invertTree(root.right)

        root.right = new_R
        root.left = new_L

        return root