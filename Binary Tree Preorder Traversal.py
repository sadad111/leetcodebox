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
#     public List<Integer> preorderTraversal(TreeNode root) {
#         List<Integer> list = new LinkedList<Integer>();
#         Stack<TreeNode> stack = new Stack<TreeNode>();
#
#         while(root != null){
#             list.add(root.val);
#             if (root.right!= null){
#                 stack.push(root.right);
#             }
#             root = root.left;
#             if (root== null && !stack.isEmpty()){
#                 root = stack.pop();
#             }
#
#         }
#         return list;
#     }
# }
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ans = []

        while root:
            ans.append(root.val)
            if root.right:
                stack.append(root.right)
            root = root.left
            if (root == None) and (len(stack)!= 0):
                root = stack.pop()
        return ans
        
