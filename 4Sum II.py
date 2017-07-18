class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
# public class Solution {
#     public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
#        Map<Integer, Integer> map = new HashMap<>();
#
#         for(int i=0; i<C.length; i++) {
#             for(int j=0; j<D.length; j++) {
#                 int sum = C[i] + D[j];
#                 map.put(sum, map.getOrDefault(sum, 0) + 1);
#             }
#         }
#
#         int res=0;
#         for(int i=0; i<A.length; i++) {
#             for(int j=0; j<B.length; j++) {
#                 res += map.getOrDefault(-1 * (A[i]+B[j]), 0);
#             }
#         }
#
#         return res;
#     }
# }
