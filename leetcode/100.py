# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: #if both null, return true
            return True

        if not p or not q: #if one is only null, return false
            return False

        if p.val!=q.val: #if numbers dont match, return false
            return False

        
        return (self.isSameTree(p.left,q.left) and
        self.isSameTree(p.right,q.right))
        