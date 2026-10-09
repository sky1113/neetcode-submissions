# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_is = {val: idx for idx, val in enumerate(inorder)}
        self.pre_i = 0

        def dfs(l, r): # inorder range
            if l > r:
                return None

            root = TreeNode(preorder[self.pre_i])
            self.pre_i += 1
            in_i = inorder_is[root.val]

            root.left = dfs(l, in_i - 1)
            root.right = dfs(in_i + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)

