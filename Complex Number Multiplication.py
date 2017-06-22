class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_int = a.split("+")
        b_int = b.split("+")
        result = []
        result[0] = int(a_int[0])*int(b_int[0]) - int(a_int[1][:-1])*int(b_int[1][:-1])
        result[1] = int(a_int[0])*int(b_int[1][:-1]) + int(b_int[0])*int(a_int[1][:-1])
        str = str(result[0]) + "+" + str(result[1]) + "i"
        return str
