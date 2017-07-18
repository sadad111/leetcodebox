class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        mask = 1
        for j in range(32):
            ones = zeros = 0
            for num in nums:
                if num & mask:
                    ones += 1
                else:
                    zeros += 1
            ans += ones * zeros
            mask = mask << 1
        return ans

# public class Solution {
#     public int totalHammingDistance(int[] nums) {
#         int total = 0, n = nums.length;
#         for (int j=0;j<32;j++) {
#             int bitCount = 0;
#             for (int i=0;i<n;i++)
#                 bitCount += (nums[i] >> j) & 1;
#             total += bitCount*(n - bitCount);
#         }
#         return total;
#     }
# }
