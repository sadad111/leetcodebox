# public class Solution {
#     private int[] nums;
#
#     public Solution(int[] nums) {
#         this.nums = nums;
#     }
#
#     /** Resets the array to its original configuration and return it. */
#     public int[] reset() {
#         return nums;
#     }
#
#     /** Returns a random shuffling of the array. */
#     public int[] shuffle() {
#         int[] rand = new int[nums.length];
#         for (int i = 0; i < nums.length; i++){
#             int r = (int) (Math.random() * (i+1));
#             rand[i] = rand[r];
#             rand[r] = nums[i];
#         }
#         return rand;
#     }
#
# }
#
# /**
#  * Your Solution object will be instantiated and called as such:
#  * Solution obj = new Solution(nums);
#  * int[] param_1 = obj.reset();
#  * int[] param_2 = obj.shuffle();
#  */
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))




# import random
# class Solution(object):
#
#     def __init__(self, nums):
#         self.nums = nums
#
#     def reset(self):
#         return self.nums
#
#     def shuffle(self):
#         ans = self.nums[:]                     # copy list
#         for i in range(len(ans)-1, 0, -1):     # start from end
#             j = random.randrange(0, i+1)    # generate random index
#             ans[i], ans[j] = ans[j], ans[i]    # swap
#         return ans
