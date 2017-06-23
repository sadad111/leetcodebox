class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: [-x[0],x[1]])
        ans = []
        for i in people:
            ans.insert(i[1],i)
        return ans
