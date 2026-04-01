# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        length = 0
        end = head
        while end is not None:
            length += 1
            end = end.next
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        count = 0

        while count < (length - n):
            prev = curr
            curr = curr.next
            count += 1
            
        prev.next = curr.next
        curr.next = None
        return dummy.next