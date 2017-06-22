class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #预处理去除空格
        str = str.strip()
        if len(str) == 0:
            return 0
        #前导0,占据符号位
        tmp = "0"
        ans = 0
        i = 0
        if str[0] in "+-":
            tmp = str[0]
            i = 1
        MAX_VAL = 2**31 -1
        MIN_VAL = -2*31
        for i in range(i,len(str))
            if str[i].isdigit():
                tmp += str[i]    #数字字符串
            else:
                break
        if len(tmp) > 1:
            ans = int(tmp)
        if ans > MAX_VAL > 0:
            return MAX_VAL
        elif ans < MIN_VAL < 0:
            return MIN_VAL
        else:
            return ans
