class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        M = collections.defaultdict(list)
        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                content = file.split('(')
                M[content[-1]].append(root + '/' + content[0])

        return [x for x in M.values() if len(x) > 1]
# java
# public class Solution {
#     public List<List<String>> findDuplicate(String[] paths) {
#         List<List<String>> result = new ArrayList<List<String>>();
#         int n = paths.length;
#         if (n == 0) return result;
#
#         Map<String, Set<String>> map = new HashMap<>();
#         for (String path : paths) {
#             String[] strs = path.split(" ");
#             for (int i = 1; i < strs.length; i++) {
#                 int idx = strs[i].indexOf("(");
#                 String content = strs[i].substring(idx);
#                 String filename = strs[0] + "/" + strs[i].substring(0, idx);
#
#                 Set<String> filenames = map.getOrDefault(content, new HashSet<String>());
#                 filenames.add(filename);
#                 map.put(content, filenames);
#             }
#         }
#
#         for (String key : map.keySet()) {
#             if (map.get(key).size() > 1) {
#                 result.add(new ArrayList<String>(map.get(key)));
#             }
#         }
#
#         return result;
#     }
# }
