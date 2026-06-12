# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=[]
        self.inorder(root,res)
        return self.issorted(res)
    def inorder(self,root,res):
        if root:
            self.inorder(root.left,res)
            res.append(root.val)
            self.inorder(root.right,res)
    def issorted(self,arr):
        if not arr:
            return False
        for i in range(1,len(arr)):
            if arr[i]<=arr[i-1]:
                return False
        return True