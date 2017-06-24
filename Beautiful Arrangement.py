class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def count(i, X):
            p = []
            if i == 1:
                return 1
            #return sum(count(i - 1, X - {x})for x in X if x % i == 0 or i % x == 0)
            for x in X:
                if x % i == 0 or i % x == 0:
                   p += [count(i-1,X-{x})]
            return sum(p)
        return count(N, set(range(1, N + 1)))
