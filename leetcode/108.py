class treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class solutions:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helper(l,r):
            if l>r:
                return None
            
            mid=(l+r)//2

            root=treenode(nums[mid])
            root.left=helper(l,mid-1)
            root.right=helper(l,mid+1)

            return root
        return helper(0,len(nums)-1)