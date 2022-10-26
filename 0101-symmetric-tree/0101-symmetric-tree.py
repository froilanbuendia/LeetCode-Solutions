# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # print(root.val)
        # if (root.left or root.right) is None:
        #     return True
        # if root.left and root.right:
        #     self.isSymmetric(root.left) == self.isSymmetric(root.right)
        # elif root.left and root.right is None:
        #     self.isSymmetric(root.left) == self.isSymmetric(root.left)
        # elif root.left is None and root.right:
        #     self.isSymmetric(root.right) == self.isSymmetric(root.right)
        # else:
        #     return False
        # return True
        def symmetric(l, r):
            if l == None and r == None:
                return True
            if (l == None or r == None) or (l.val != r.val):
                return False
            return symmetric(l.left, r.right) and symmetric(l.right, r.left)
                
        return symmetric(root, root)
            
        
        