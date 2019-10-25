class Solution:
    def simplifyPath(self, path):
        stack = [] 
        for c in path.split("/"):
            stack = stack[:-1] if c== ".." else stack + [c] if c and c != "." else stack
        return "/" + "/".join(stack)