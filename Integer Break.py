# public class Solution {
#     public int integerBreak(int n) {
#         if(n==2) return 1;
#         if(n==3) return 2;
#         int product = 1;
#         while(n>4){
#             product*=3;
#             n-=3;
#         }
#         product*=n;
#
#         return product;
#     }
# }
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        res_list = [2,3,4]
        if n<4: return res_list[n-2]-1
        f= lambda x: res_list[x-2] if x<=4 else 3*f(x-3)
        return f(n)
