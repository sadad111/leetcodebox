# /**
#  * Definition for singly-linked list.
#  * public class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode(int x) { val = x; }
#  * }
#  */
# public class Solution {
#     public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
#         Stack<Integer> s1 = new Stack<Integer>();
#         Stack<Integer> s2 = new Stack<Integer>();
#
#         while(l1 != null) {
#             s1.push(l1.val);
#             l1 = l1.next;
#         };
#         while(l2 != null) {
#             s2.push(l2.val);
#             l2 = l2.next;
#         }
#
#         int sum = 0;
#         ListNode list = new ListNode(0);
#         while (!s1.empty() || !s2.empty()) {
#             if (!s1.empty()) sum += s1.pop();
#             if (!s2.empty()) sum += s2.pop();
#             list.val = sum % 10;
#             ListNode head = new ListNode(sum / 10);
#             head.next = list;
#             list = head;
#             sum /= 10;
#         }
#
#         return list.val == 0 ? list.next : list;
#     }
# }
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1,stack2 = [],[]
        while l1:
            stack1.append(l1.val)
            l1=l1.next

        while l2:
            stack2.append(l2.val)
            l2=l2.next

        sum_num = 0
        list_node = ListNode(0)
        while stack1 or stack2:
            if stack1:
                sum_num += stack1.pop()
            if stack2:
                sum_num += stack2.pop()
            list_node.val = sum_num % 10
            head = ListNode(sum_num//10)
            head.next = list_node
            list_node = head
            sum_num //= 10

        return head if head.val != 0 else head.next
                
