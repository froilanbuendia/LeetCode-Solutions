# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = ListNode()
        node = nodes
        while (list1 and list2) is not None:
            if list1.val < list2.val:
                node.next = list1
                node = node.next
                list1 = list1.next
            else:
                node.next = list2
                node = node.next
                list2 = list2.next
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
        return nodes.next
    
    