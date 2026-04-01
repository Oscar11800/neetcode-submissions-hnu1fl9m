class ListNode:
    def __init__(self, key = 0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        """Initialize LRU cache of given capacity."""
        self.capacity = capacity
        self.hash_map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        if node == self.head or node == self.tail:
            return
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
        node.next = None
        node.prev = None
    
    def _add_to_tail(self, node):
        if node == self.head or node == self.tail:
            return
        old_tail = self.tail.prev
        new_tail = node
        old_tail.next = new_tail
        new_tail.prev = old_tail
        new_tail.next = self.tail
        self.tail.prev = new_tail

    def _move_to_tail(self, node):
        if node == self.head or node == self.tail:
            return
        self._remove(node)
        self._add_to_tail(node)

    def _pop_head(self):
        if self.head.next != self.tail:
            rtn = self.head.next
            self._remove(self.head.next)
            return rtn
        else:
            return None

    def get(self, key: int) -> int:
        """Return value for key if exists, else -1."""
        if key in self.hash_map:
            # update MRU
            self._move_to_tail(self.hash_map[key])
            return self.hash_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """Insert or update. Evict LRU if over capacity."""
        # already exists
        if key in self.hash_map:
            # update value
            curr_node = self.hash_map.get(key)
            curr_node.val = value
            # set to be MRU
            self._move_to_tail(curr_node)
        # does not exist
        else: 
            # evict if size reached
            if len(self.hash_map) == self.capacity:
                # evict and remove
                del self.hash_map[self._pop_head().key]
                # add new node
                curr_node = ListNode(key, value)
                self.hash_map[key] = curr_node
                # add to MRU
                self._add_to_tail(curr_node)
            else:
                curr_node = ListNode(key, value)
                self.hash_map[key] = curr_node
                self._add_to_tail(curr_node)