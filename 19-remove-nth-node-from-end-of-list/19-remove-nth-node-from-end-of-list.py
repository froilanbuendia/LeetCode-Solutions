# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = ListNode(0, head)
        left = node
        right = head
        # 1) decrement n until 0 and move right pointer to next point
        while n > 0:
            right = right.next
            n -= 1
        # 2) go until right is none
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return node.next
        