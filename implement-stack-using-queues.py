class MyStack:

    def __init__(self):
        self.primary_queue = deque()
        self.temp_queue = deque()

    def push(self, x: int) -> None:
        
        while self.primary_queue:
            self.temp_queue.append(self.primary_queue.popleft())
        
       
        self.primary_queue.append(x)
        
        
        while self.temp_queue:
            self.primary_queue.append(self.temp_queue.popleft())

    def pop(self) -> int:
        return self.primary_queue.popleft()

    def top(self) -> int:
        return self.primary_queue[0]

    def empty(self) -> bool:
        return len(self.primary_queue) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
