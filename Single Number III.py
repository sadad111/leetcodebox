# public class Solution {
#     public int[] singleNumber(int[] nums) {
#            // Pass 1 :
#         // Get the XOR of the two numbers we need to find
#         int diff = 0;
#         for (int num : nums) {
#             diff ^= num;
#         }
#         // Get its last set bit
#         diff &= -diff;
#
#         // Pass 2 :
#         int[] rets = {0, 0}; // this array stores the two numbers we will return
#         for (int num : nums)
#         {
#             if ((num & diff) == 0) // the bit is not set
#             {
#                 rets[0] ^= num;
#             }
#             else // the bit is set
#             {
#                 rets[1] ^= num;
#             }
#         }
#         return rets;
#     }
# }
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
        mask = 1
        while(xor&mask == 0):
            mask = mask << 1
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
