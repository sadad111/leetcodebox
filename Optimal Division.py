class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 0:
            return ""
        elif len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            ans = str(nums[0]) + "/("
            for i in nums[1:-1]:
                ans += str(i) +"/"
            ans += str(nums[-1]) + ")"
            return ans
