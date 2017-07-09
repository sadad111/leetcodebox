class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        listreq = [False]*l
        ans = 0
        for k in range(l):
            count = 0
            t = k
            while not listreq[t]:
                listreq[t] = True
                count += 1
                t =  nums[t]
            if count == l:
                return count
            ans = max(ans,count)
        return ans


# public class Solution {
#     public int arrayNesting(int[] nums) {
#         int res = 0;
#         for (int i=0;i<nums.length;i++) {
#             if (nums[i] < 0) continue;
#             int length = 1, val = nums[i];
#             while (Math.abs(val) != i) {
#                 length++;
#                 val = nums[Math.abs(val)];
#                 nums[Math.abs(val)] *= -1;
#             }
#             res = Math.max(res, length);
#         }
#         return res;
#     }
# }
