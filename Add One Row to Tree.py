# /**
#  * Definition for a binary tree node.
#  * public class TreeNode {
#  *     int val;
#  *     TreeNode left;
#  *     TreeNode right;
#  *     TreeNode(int x) { val = x; }
#  * }
#  */
# public class Solution {
#     public TreeNode addOneRow(TreeNode root, int v, int d) {
#         if (d < 2) {
#             TreeNode newroot = new TreeNode(v);
#             if (d == 0) newroot.right = root;
#             else newroot.left = root;
#             return newroot;
#         }
#         if (root == null) return null;
#         root.left = addOneRow(root.left, v, d == 2 ? 1 : d-1);
#         root.right = addOneRow(root.right, v, d == 2 ? 0 : d-1);
#         return root;
#     }
# }
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        for _ in range(d - 1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return dummy.left
