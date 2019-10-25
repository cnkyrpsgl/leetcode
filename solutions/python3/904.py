class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = i = 0
        last = collections.defaultdict(int)
        for j, val in enumerate(tree):
            if len(last) == 2 and val not in last:
                pre = min(last.values())
                i = pre + 1
                last.pop(tree[pre])
            last[val] = j
            res = max(res, j - i + 1)
        return res