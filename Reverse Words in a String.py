class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = s.split(" ")
        strs = strs.reverse()
        ans = ""
        if len(strs) >= 1:
            for i in strs:
                ans += i + " "
            print (ans)
        return ans.rstrip()
