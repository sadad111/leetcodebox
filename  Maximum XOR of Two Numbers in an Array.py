# public class Solution {
#     public int findMaximumXOR(int[] nums) {
#         int max = 0, mask = 0;
#         for(int i = 31; i >= 0; i--){
#             mask = mask | (1 << i);
#             Set<Integer> set = new HashSet<>();
#             for(int num : nums){
#                 set.add(num & mask);
#             }
#             //System.out.println(set);
#             int tmp = max | (1 << i);
#             for(int prefix : set){
#                 if(set.contains(tmp ^ prefix)) {
#                     max = tmp;
#                     //System.out.println(max);
#                     break;
#                 }
#             }
#         }
#         return max;
#     }
# }
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans,mask = 0,0
        for i in range(32)[::-1]:
            mask |= 1<<i
            prefixes = {num&mask for num in nums}
            tmp = 1<<i | ans
            for j in prefixes:
                if j^tmp in prefixes:
                    ans = tmp
                    # print ans
                    break
        return ans
