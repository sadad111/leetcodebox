# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        def getSum(node):
        	if node == None: return 0
        	s = node.val + getSum(node.left) + getSum(node.right)
        	c[s]+= 1
        	return s
        c = collections.Counter()
        getSum(root)
        frequent = max(c.values())
        return [s for s in c.keys() if c[s] == frequent]


# 
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
#     Map<Integer, Integer> sumToCount;
#     int maxCount;
#
#     public int[] findFrequentTreeSum(TreeNode root) {
#         maxCount = 0;
#         sumToCount = new HashMap<Integer, Integer>();
#
#         postOrder(root);
#
#         List<Integer> res = new ArrayList<>();
#         for (int key : sumToCount.keySet()) {
#             if (sumToCount.get(key) == maxCount) {
#                 res.add(key);
#             }
#         }
#
#         int[] result = new int[res.size()];
#         for (int i = 0; i < res.size(); i++) {
#             result[i] = res.get(i);
#         }
#         return result;
#     }
#
#     private int postOrder(TreeNode root) {
#         if (root == null) return 0;
#
#         int left = postOrder(root.left);
#         int right = postOrder(root.right);
#
#         int sum = left + right + root.val;
#         int count = sumToCount.getOrDefault(sum, 0) + 1;
#         sumToCount.put(sum, count);
#
#         maxCount = Math.max(maxCount, count);
#
#         return sum;
#     }
# }
