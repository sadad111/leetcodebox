class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, res = [], [-1] * len(nums)
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res
# public class Solution {
#     public int[] nextGreaterElements(int[] nums) {
#         if(nums == null || nums.length == 0) return new int[0];
#         int[] ret = new int[nums.length];
#         Arrays.fill(ret,-1);
#         Stack<Integer> stack = new Stack<>();
#         for(int j =0; j<=1; j++){
#             for(int i = 0; i <nums.length ; i++){
#             while(!stack.isEmpty() && nums[stack.peek()] < nums[i])
#                 ret[stack.pop()] = nums[i];
#             stack.push(i);
#             }
#         }
#         return ret;
#     }
# }
