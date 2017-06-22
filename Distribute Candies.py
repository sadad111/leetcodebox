class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        result = 0
        kind = list(set(candies))
        if len(kind) > len(candies)/2:
            result = len(candies)/2
        else:
            result = len(kind)
        return result
