class Solution:
    def exclusiveTime(self, n, logs):
        res, stack = [0] * n, []
        for log in logs:
            log = log.split(":")
            if log[1] == "start":
                stack.append([int(log[2]), 0])
            else:
                start = stack.pop()
                time = int(log[2]) - start[0] + 1
                res[int(log[0])] += time - start[1]
                if stack:
                    stack[-1][1] += time
        return res