class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store all values
        self.min_stack = []  # Auxiliary stack to store the minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or the new value is smaller or equal, push it onto min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the top value from the main stack
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the same as the top of min_stack, pop it from min_stack too
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top value from the main stack
        if self.stack:
            return self.stack[-1]
        return None  # Or raise an exception if you prefer

    def getMin(self) -> int:
        # Return the top value from the min_stack
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Or raise an exception if you prefer
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
