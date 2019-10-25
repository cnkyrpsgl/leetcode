class Solution:
    def calculate(self, s):
        def calc(n2, op, n1): 
            return n1 + n2 if op == "+" else n1 - n2
        stack, i, num = [], 0, 0
        while i < len(s):
            j = i
            while j < len(s) and s[j].isdigit():
                num, j = num * 10 + int(s[j]), j + 1
            if i != j:
                stack.append(calc(num, stack.pop(), stack.pop()) if stack and s[i - 1] != "(" else num)
                num, j = 0, j - 1
            elif s[i] in "+-":
                stack.append(s[i])
            elif s[i] == ")" and len(stack) > 1:
                stack.append(calc(stack.pop(), stack.pop(), stack.pop()))
            i = j + 1
        return stack.pop()