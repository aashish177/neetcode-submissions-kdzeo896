class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        stack2 = []
        stack2 = self.stack[0:len(self.stack)-1]
        self.stack = stack2

    def top(self) -> int:
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        val = min(self.stack)
        return val
