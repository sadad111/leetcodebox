# public class Solution {
#     public int magicalString(int n) {
#         if (n <= 0) return 0;
#         if (n <= 3) return 1;
#         int result = 1;
#         int[] a = new int[n+3];
#         a[0]=1;a[1]=2;a[2]=2;
#         int tail =2; int flag =2;
#         while(a[n-1]==0){
#             int next_tmp = a[tail] == 1 ? 2:1;
#             if (next_tmp==1)result += a[flag];
#             int count = a[flag];
#             for (int i=0; i<count ; i++){
#                 tail += 1;
#                 a[tail] = next_tmp;
#             }
#             flag+=1;
#         }
#         if(a[n]==1)result-=1;
#         return result;
#     }
#
# }

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = "122"
        flag = 2
        while len(s) < n:
            nxt = '2' if s[-1]=='1' else '1'
            s+= int(s[flag])*nxt
            flag += 1
        return collections.Counter(s[:n])['1']
