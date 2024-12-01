class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val not in ('+', '-', '*', '/'):
                # Push numbers onto the stack
                stack.append(int(val))  # Convert to integer before appending
                # print(stack)
            else:
                # Pop the top two numbers for the operator
                b = stack.pop()  # Second operand
                a = stack.pop()  # First operand
                
                # Perform the operation
                if val == '+':
                    res = a + b
                elif val == '-':
                    res = a - b
                elif val == '*':
                    res = a * b
                elif val == '/':
                    res = int(a / b)  # Integer division as per RPN
                
                # Push the result back onto the stack
                stack.append(res)

        # Final result will be the only item left on the stack
        return stack[-1]
                