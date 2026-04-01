# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list.

        :param lists: Array of linked list heads (each list is sorted ascending).
        :return: Head of the merged sorted linked list.
        """
        heap = []
        id = 0
        # initialize the heap
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, id, l))
                id += 1
        dummy = ListNode()
        curr = dummy
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id, node.next))
            id += 1
        return dummy.next