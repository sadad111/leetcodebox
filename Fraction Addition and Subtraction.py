# public class Solution {
#     public String fractionAddition(String expression) {
#         Scanner sc = new Scanner(expression).useDelimiter("/|(?=[-+])");
#         int A = 0, B = 1;
#         while (sc.hasNext()) {
#             int a = sc.nextInt(), b = sc.nextInt();
#             A = A * b + a * B;
#             B *= b;
#             int g = gcd(A, B);
#             A /= g;
#             B /= g;
#         }
#         return A + "/" + B;
#     }
#
#     private int gcd(int a, int b) {
#         return a != 0 ? gcd(b % a, a) : Math.abs(b);
#     }
# }
class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        ints = iter(ints)
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)
