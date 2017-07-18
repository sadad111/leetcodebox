# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# /**
#  * Definition for singly-linked list.
#  * public class ListNode {
#  *     int val;
#  *     ListNode next;
#  *     ListNode(int x) { val = x; }
#  * }
#  */
# public class Solution {
#
#     ListNode h;
#     Random random;
#     /** @param head The linked list's head.
#         Note that the head is guaranteed to be not null, so it contains at least one node. */
#     public Solution(ListNode head) {
#         h = head;
#         random = new Random();
#     }
#
#     /** Returns a random node's value. */
#     public int getRandom() {
#         ListNode c = h;
#         int r = c.val;
#         for(int i=1;c.next != null;i++){
#
#             c = c.next;
#             if(random.nextInt(i + 1) == i) r = c.val;
#         }
#
#         return r;
#     }
# }
#
# /**
#  * Your Solution object will be instantiated and called as such:
#  * Solution obj = new Solution(head);
#  * int param_1 = obj.getRandom();
#  */
