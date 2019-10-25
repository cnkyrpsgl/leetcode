class Solution:
    def calculate(self, s):
        mod = 0
        while mod < 2:
            stack, i, n, num = [], 0, len(s), ""
            while i < n:
                if s[i] == " ":
                    i += 1
                    continue
                while mod == 0 and i < n and s[i].isnumeric():
                    num += s[i]
                    i += 1
                if stack and stack[-1] in [("*", "/"), ("+", "-")][mod]:
                    op, num1 = stack.pop(), stack.pop()
                    if op == "*":
                        stack.append(num1 * int(num))
                    elif op == "/":
                        stack.append(num1 // int(num))
                    elif op == "+":
                        stack.append(num1 + s[i])
                        i += 1
                    else:
                        stack.append(num1 - s[i])
                        i += 1
                    num = ""
                elif num:
                    stack.append(int(num))
                    num = ""
                else:
                    stack.append(s[i])
                    i += 1
            mod += 1
            s = stack
        return stack.pop()