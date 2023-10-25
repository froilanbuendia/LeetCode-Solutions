# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            # temp right of curr
            temp = curr.next
            # right of curr becomes left of curr
            curr.next = prev
            # prev is curr
            prev = curr
            # curr is right of temp
            curr = temp
        return prev