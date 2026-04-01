# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        lp1 = list1
        lp2 = list2
        while lp1 or lp2:
            if lp1 and lp2:
                if lp1.val <= lp2.val:
                    curr.next = lp1
                    lp1 = lp1.next
                else:
                    curr.next = lp2
                    lp2 = lp2.next
            elif lp1 and not lp2:
                curr.next = lp1
                lp1 = lp1.next
            else:
                curr.next = lp2
                lp2 = lp2.next
            curr = curr.next
        return dummy.next