class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        space_num = []
        ans = 0
        count = 0
        length = 0
        for i in range(1,len(A)):
            space_num += [A[i]-A[i-1]]
        # print space_num
        for i in range(1,len(space_num)):
            if space_num[i] == space_num[i-1]:
                count += 1
                length += 1
            else:
                ans += count + sum(list(range(length)))
                count = 0
                length = 0
        ans += count + sum(list(range(length)))
        return ans
