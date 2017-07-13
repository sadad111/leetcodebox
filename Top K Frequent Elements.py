# public class Solution {
#     public List<Integer> topKFrequent(int[] nums, int k) {
#         Map<Integer, Integer> map = new HashMap<>();
#         for(int n: nums){
#             map.put(n, map.getOrDefault(n,0)+1);
#         }
#
#         PriorityQueue<Map.Entry<Integer, Integer>> maxHeap =
#                          new PriorityQueue<>((a,b)->(b.getValue()-a.getValue()));
#         for(Map.Entry<Integer,Integer> entry: map.entrySet()){
#             maxHeap.add(entry);
#         }
#
#         List<Integer> res = new ArrayList<>();
#         while(res.size()<k){
#             Map.Entry<Integer, Integer> entry = maxHeap.poll();
#             res.add(entry.getKey());
#         }
#         return res;
#     }
# }
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [i[0] for i in collections.Counter(nums).most_common(k)]
