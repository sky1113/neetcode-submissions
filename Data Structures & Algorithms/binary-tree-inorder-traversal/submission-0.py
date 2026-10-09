# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        def traverse(root, lst):
            if not root:
                return

            traverse(root.left, lst)
            lst.append(root.val)
            traverse(root.right, lst)

            return lst
        
        res = traverse(root, res)
        return res