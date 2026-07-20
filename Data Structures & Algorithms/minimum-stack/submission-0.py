class MinStack:

    def __init__(self):
        self.stack = []
        self.helper_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.helper_stack:
            self.helper_stack.append(val)
        else:
            self.helper_stack.append(min(val, self.helper_stack[-1]))
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.helper_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return 0
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.helper_stack:
            return 0
        else:
            return self.helper_stack[-1]
        
