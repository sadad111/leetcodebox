class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        h = len(nums)
        w = len(nums[0])
        if h*w != r*c:
            return nums
        else:
            nums_fla = [y for x in nums for y in x]
            ans = []
            for i in range(r):
                bns = []
                for j in range(c):
                    bns += [nums_fla[i*c+j]]
                ans.append(bns)
        return ans
