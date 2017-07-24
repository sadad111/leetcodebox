# public class Solution {
#     public int leastBricks(List<List<Integer>> wall) {
#         int row = wall.size();
#         if (row == 0)   return 0;
#         else{
#             int col = wall.get(0).size();
#             if (col == 0)   return 0;
#             else{
#                 HashMap<Integer, Integer> map = new HashMap<>();
#                 for(int i = 0; i < row; i++){
#                     int width = 0;
#                     for(int j = 0; j < wall.get(i).size() - 1; j++){
#                         width+=wall.get(i).get(j);
#                         if (map.containsKey(width) ){
#                             map.put(width, map.get(width) + 1);
#                         }
#                         else
#                             map.put(width, 1);
#                     }
#                 }
#                 int max = 0;
#                 for(int key : map.keySet()){
#                     max = Math.max(max, map.get(key));
#                 }
#                 return row - max;
#             }
#         }
#     }
# }
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        # print len(wall), d
        return len(wall)-max(d.values()+[0])
        
