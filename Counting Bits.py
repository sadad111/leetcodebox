class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # f[i] = f[i >> 2] + i & 1.
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
            print res
        return res[:num+1]
