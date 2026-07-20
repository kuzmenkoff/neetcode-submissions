class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
                continue
            if len(stack) == 0:
                return False
            elif ch == ')' and stack.pop() != '(':
                return False
            elif ch == '}' and stack.pop() != '{':
                return False
            elif ch == ']' and stack.pop() != '[':
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False


            

        