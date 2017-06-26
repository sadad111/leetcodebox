class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        dict_num = {}
        for i in nums:
            if i in dict_num:
                ans += [i]
            else:
                dict_num[i] = 1
        return ans
