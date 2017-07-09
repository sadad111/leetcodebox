# public class Solution {
#     public int minMoves2(int[] nums) {
#         Arrays.sort(nums);
#         int i = 0, j = nums.length-1;
#         int count = 0;
#         while(i < j){
#             count += nums[j]-nums[i];
#             i++;
#             j--;
#         }
#         return count;
#
#     }
# }

# class Solution(object):
#     def minMoves2(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         return sum(nums[-i-1] - nums[i] for i in range(len(nums) / 2))
