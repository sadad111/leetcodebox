# public class Solution {
#     public int countNumbersWithUniqueDigits(int n) {
#         if(n==0) return 1;
#         int res = 10;
#         if (n==1) return res;
#         int unic = 9;
#         if (n<=10){
#             int tmp = 9;
#             for(int i =2 ; i<=n ; i++){
#                 tmp *=unic;
#                 unic -= 1;
#                 res += tmp;
#             }
#             return res;
#         }
#        else{
#             return 0;
#        }
#
#     }
# }
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s= [9,9,8,7,6,5,4,3,2,1,0]
        f = lambda x : 1 if x==0 else s[x-1]*f(x-1)
        if n==0 :return f(0)
        if n>=11 : return 0
        res = 1
        for i in range(1,n+1):
            res +=f(i)
        return res
