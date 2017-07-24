# public class Solution {
#     public List<String> generateParenthesis(int n) {
#         List<String> list = new ArrayList<String>();
#         backtrack(list, "", 0, 0, n);
#         return list;
#     }
#
#     public void backtrack(List<String> list, String str, int open, int close, int max){
#
#         if(str.length() == max*2){
#             list.add(str);
#             return;
#         }
#
#         if(open < max)
#             backtrack(list, str+"(", open+1, close, max);
#         if(close < open)
#             backtrack(list, str+")", open, close+1, max);
#     }
# }
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)


#逗号表示truple
