# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode()
        current.next = head

        dummy = None
        after = current.next
        current.next = dummy
        current = after

        reverse = None
        while current:
            after = current.next
            current.next = reverse
            reverse = current
            current = after
        

        return reverse
