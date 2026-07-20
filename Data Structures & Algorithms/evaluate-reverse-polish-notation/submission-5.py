class Solution:
    def __init__(self):
        self.stack = []

    def evalRPN(self, tokens: List[str]) -> int:
        for token in tokens:
            if not self.is_operator(token):
                self.stack.append(int(token))
            else: 
                if token == '+':
                    self.add()
                elif token == '-':
                    self.substract()
                elif token == '*':
                    self.multiply()
                elif token == '/':
                    self.divide()
        return self.stack.pop()


    def is_operator(self, token):
        return token in ['+', '-', '*', '/']
    
    def add(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def substract(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)
    
    def multiply(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)

    def divide(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(int(a / b))

        