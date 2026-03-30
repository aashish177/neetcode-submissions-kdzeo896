class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        res = 0
        for t in tokens:
            if t == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))

            elif t == "-":
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a-b)
            
            elif t == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            
            elif t == "/":
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(int(float(a) / b))
            else:
                stack.append(int(t))
        return stack[-1]