# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class solution:
    def max_depth(self,root):
        if not root: return 0


        left=self.max_depth(root.left)
        right=self.max_depth(root.right)

        return 1+max(left,right)