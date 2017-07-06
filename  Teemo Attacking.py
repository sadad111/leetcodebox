# public class Solution {
#     public int findPoisonedDuration(int[] timeSeries, int duration) {
#         int result = 0;
#
#         if(timeSeries.length==0) return 0;
#         if(timeSeries.length==1) return duration;
#
#         for (int i =1 ; i < timeSeries.length; i++){
#             if (timeSeries[i]-timeSeries[i-1]>= duration)
#             {
#                 result += duration;
#             }
#             else if(timeSeries[i]-timeSeries[i-1]<duration && timeSeries[i]-timeSeries[i-1] >=0)
#             {
#                 result += timeSeries[i]-timeSeries[i-1];
#             }
#             else{
#                result += timeSeries[i]-timeSeries[i-1];
#             }
#         }
#
#         result += duration;
#         return result;
#     }
# }
#
#
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = duration * len(timeSeries)
        for i in range(1,len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans
