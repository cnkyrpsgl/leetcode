class Solution:
    def killProcess(self, pid, ppid, kill):
        indexes, res = collections.defaultdict(list), [kill]
        for i, p in enumerate(ppid):
            indexes[p].append(i)
        stack = [kill]
        while stack:
            for i in indexes[stack.pop()]:
                res.append(pid[i])
                stack.append(pid[i])
        return res