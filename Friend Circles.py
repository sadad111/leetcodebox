#
#
# public class Solution {
#      class UnionFind {
#         private int count = 0;
#         private int[] parent, rank;
#
#         public UnionFind(int n) {
#             count = n;
#             parent = new int[n];
#             rank = new int[n];
#             for (int i = 0; i < n; i++) {
#                 parent[i] = i;
#             }
#
#         }
#
#         public int find(int p) {
#         	while (p != parent[p]) {
#                 parent[p] = parent[parent[p]];    // path compression by halving
#                 p = parent[p];
#             }
#             return p;
#         }
#
#         public void union(int p, int q) {
#             int rootP = find(p);
#             int rootQ = find(q);
#             if (rootP == rootQ) return;
#             if (rank[rootQ] > rank[rootP]) {
#                 parent[rootP] = rootQ;
#             }
#             else {
#                 parent[rootQ] = rootP;
#                 if (rank[rootP] == rank[rootQ]) {
#                     rank[rootP]++;
#                 }
#             }
#             count--;
#         }
#
#         public int count() {
#             return count;
#         }
#     }
#
#
#     public int findCircleNum(int[][] M) {
#         int n = M.length;
#         UnionFind uf = new UnionFind(n);
#         for (int i = 0; i < n - 1; i++) {
#             for (int j = i + 1; j < n; j++) {
#                 if (M[i][j] == 1) uf.union(i, j);
#             }
#         }
#         return uf.count();
#
#     }
# }

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(M[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        for i in xrange(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
