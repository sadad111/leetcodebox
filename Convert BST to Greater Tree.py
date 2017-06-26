# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val = 0
        def visit(root):
            if root:
                visit(root.right)
                root.val += self.val
                self.val = root.val
                visit(root.left)
        visit(root)
        return root
