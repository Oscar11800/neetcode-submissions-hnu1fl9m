# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None or head.next.next is None:
            return
        # 1. get to middle
        slow= head
        fast = head
        firsthead = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2. split the lists
        secondhead = slow.next
        slow.next = None
        # 3. reverse the second list
        first = None
        second = secondhead
        while second:
            temp = first
            first = second
            second = second.next
            first.next = temp
        # 4. Now do the alternating linking
        fp = firsthead
        sp = first
        while sp:
            n1 = fp.next
            n2 = sp.next

            fp.next = sp
            sp.next = n1

            fp = n1
            sp = n2