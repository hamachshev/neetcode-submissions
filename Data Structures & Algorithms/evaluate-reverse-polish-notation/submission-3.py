class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token == "+":
                operand2 = stack.pop()
                operand1= stack.pop()
                stack.append(operand1 + operand2)
            elif token == "-":
                operand2 = stack.pop()
                operand1= stack.pop()
                stack.append(operand1 - operand2)
            elif token == "*":
                operand2 = stack.pop()
                operand1= stack.pop()
                stack.append(operand1 * operand2)
            elif token == "/":
                operand2 = stack.pop()
                operand1= stack.pop()
                res = operand1 / operand2
                stack.append(int(res))
            else:
                stack.append(int(token))
        
        return stack.pop()