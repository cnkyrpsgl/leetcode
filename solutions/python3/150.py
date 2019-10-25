class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"): stack.append(int(token))
            else:
                num2, num1 = stack.pop(), stack.pop()
                if token == "+": last = num1 + num2
                elif token == "-": last = num1 - num2
                elif token == "*": last = num1 * num2
                elif token == "/": last = int(num1 / num2)
                stack.append(last)
        return stack[0]