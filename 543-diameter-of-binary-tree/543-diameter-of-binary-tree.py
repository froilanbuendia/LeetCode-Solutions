# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def depth(root):
            if root is None: return 0
            l = depth(root.left)
            r = depth(root.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)
        depth(root)
        return self.res
    