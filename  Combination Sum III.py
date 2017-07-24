import itertools
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k>= n : return []
        # combs = [[]]
        # for _ in range(k):
        #     combs = [[first] + comb for comb in combs for first in range(1, comb[0] if comb else 10)]
        return [c for c in itertools.combinations(range(1, 10), k) if sum(c) == n]
        # return [c for c in combs if sum(c) == n]
        
