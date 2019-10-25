class NumArray:
    def __init__(self, nums):
        if nums:
            self.n = len(nums)
            self.tree = [0] * (2 * (2 ** int(math.ceil(math.log(self.n, 2)))) - 1)
            def dfs(node, s, e):
                if s == e: self.tree[node] = nums[s]
                else:
                    m = (s + e) // 2
                    dfs(2 * node + 1, s, m)
                    dfs(2 * node + 2, m + 1, e)
                    self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
            dfs(0, 0, self.n - 1)
    def update(self, i, val):
        def dfs(node, s, e, idx, val):
            if s == e: self.tree[node] = val
            else:
                m = (s + e) // 2
                if s <= idx <= m: dfs(2 * node + 1, s, m, idx, val)
                else: dfs(2 * node + 2, m + 1, e, idx, val)
                self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        dfs(0, 0, self.n - 1, i, val)
    def sumRange(self, i, j):
        def dfs(node, s, e, l, r):
            if r < s or l > e: return 0
            if l <= s and e <= r: return self.tree[node]
            m = (s + e) // 2
            return dfs(2 * node + 1, s, m, l, r) + dfs(2 * node + 2, m + 1, e, l, r)
        return dfs(0, 0, self.n - 1, i, j)