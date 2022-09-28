# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
            
        while (fast != None and fast.next != None):
            fast = fast.next
            slow = slow.next
            
        if fast == None:
            return slow.next
        else:
            slow.next = slow.next.next
            
        return head
        