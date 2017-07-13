# public class LogSystem {
#
#     List<String[]> timestamps = new LinkedList<>();
#     List<String> units = Arrays.asList("Year", "Month", "Day", "Hour", "Minute", "Second");
#     int[] indices = new int[]{4,7,10,13,16,19};
#
#     public void put(int id, String timestamp) { timestamps.add(new String[]{Integer.toString(id), timestamp}); }
#
#     public List<Integer> retrieve(String s, String e, String gra) {
#         List<Integer> res = new LinkedList<>();
#         int idx = indices[units.indexOf(gra)];
#         for (String[] timestamp : timestamps) {
#             if (timestamp[1].substring(0, idx).compareTo(s.substring(0, idx)) >= 0 &&
#                	timestamp[1].substring(0, idx).compareTo(e.substring(0, idx)) <= 0) res.add(Integer.parseInt(timestamp[0]));
#         }
#         return res;
#     }
# }
class LogSystem(object):

    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.logs.append((id,timestamp))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        index = {'Year': 5, 'Month': 8, 'Day': 11,
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]

        start = s[:index]
        end = e[:index]

        return sorted(tid for tid , timestamp in self.logs
                        if start <= timestamp[:index] <= end)

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
