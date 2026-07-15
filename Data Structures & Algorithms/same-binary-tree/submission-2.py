# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            if not q:
                return True
            return False
        if not q:
            return False

        pq = deque([p])
        qq = deque([q])

        while pq and qq:
            pcurr = pq.pop()
            qcurr = qq.pop()

            if pcurr.val != qcurr.val:
                return False
            
            if pcurr.left:
                if not qcurr.left:
                    return False
                pq.append(pcurr.left)
            if qcurr.left:
                if not pcurr.left:
                    return False
                qq.append(qcurr.left)
            if pcurr.right:
                if not qcurr.right:
                    return False
                pq.append(pcurr.right)
            if qcurr.right:
                if not pcurr.right:
                    return False
                qq.append(qcurr.right)

        return True