class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s0='#'+'#'.join(s)+'#'
        res=""
        current = 0
        RL=[0]*len(s0)
        MaxRight=0
        pos=0
        MaxLen=0
        for i in range(len(s0)):
            if i<MaxRight:
                RL[i]=min(RL[2*pos-i], MaxRight-i)
            else:
                RL[i]=1
            #尝试扩展，注意处理边界
            while i-RL[i]>=0 and i+RL[i]<len(s0) and s0[i-RL[i]]==s0[i+RL[i]]:
                RL[i]+=1
            #更新MaxRight,pos
            if RL[i]+i-1>MaxRight:
                MaxRight=RL[i]+i-1
                pos=i
            #更新最长回文串的长度
            MaxLen=max(MaxLen, RL[i])
            if MaxLen == RL[i]:
                current = i
                res = s[(i-MaxLen)//2+1:(i+MaxLen)//2]
        return res
