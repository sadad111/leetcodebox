# public class Solution {
#     public int[] productExceptSelf(int[] nums) {
#         int n = nums.length;
#         int[] res = new int[n];
#         res[0] = 1;
#         for (int i = 1; i < n; i++) {
#             res[i] = res[i - 1] * nums[i - 1];
#         }
#         int right = 1;
#         for (int i = n - 1; i >= 0; i--) {
#             res[i] *= right;
#             right *= nums[i];
#         }
#         return res;
#         }
# }
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
