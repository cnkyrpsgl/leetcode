class Solution:
    def decodeString(self, s):
        stack, num, string = [], 0, ""
        for c in s:
            if c == "[":
                stack += string,
                stack += num,
                num, string = 0, ""
            elif c == "]":
                pre_num, pre_string = stack.pop(), stack.pop()
                string = pre_string + pre_num * string
            elif c.isdigit(): num = num * 10 + int(c)
            else: string += c
        return string