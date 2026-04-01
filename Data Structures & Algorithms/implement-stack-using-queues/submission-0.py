class MyStack:
    def __init__(self):
        """Initialize two queues."""
        self.q1 = deque()
        self.q2 = deque()
        self.toggle = 0
        self.size = 0

    def push(self, x: int) -> None:
        """Push element x to the top of the stack."""
        # first move everything from q1 to q1, then push element and then push back into q1
        if not self.toggle: # q1 has stuff
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())
            self.toggle = 1
        else:
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())
            self.toggle = 0
        self.size += 1


    def pop(self) -> int:
        """Remove and return the element on top of the stack."""
        if not self.toggle:
            self.size -= 1
            return self.q1.popleft()
        else:
            self.size -= 1
            return self.q2.popleft()
        


    def top(self) -> int:
        """Return the element on top of the stack without removing it."""
        if not self.toggle:
            return self.q1[0]
        else:
            return self.q2[0]

    def empty(self) -> bool:
        """Return True if the stack is empty, False otherwise."""
        return self.size == 0