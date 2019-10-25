class Solution:
    def isLongPressedName(self, name, typed):
        pre, i = None, 0
        for c in typed:
            if i < len(name) and c == name[i]:
                pre, i = name[i], i + 1
            elif c != pre:
                return False
        return i == len(name)