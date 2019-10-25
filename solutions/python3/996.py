class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        self.res = 0
        def dfs(cnt, num):
            if not cnt:
                self.res += 1
            for new in nex[num]:
                if cnt[new]:
                    cnt[new] -= 1
                    if not cnt[new]:
                        cnt.pop(new)
                    dfs(cnt, new)
                    cnt[new] += 1
            
        nex = collections.defaultdict(set)  
        cnt = collections.Counter(A)
        for a, b in itertools.permutations(A, 2):
            if not (a + b) ** 0.5 % 1:
                nex[a].add(b)
                nex[b].add(a)
        for a in set(A):
            cnt[a] -= 1
            if not cnt[a]:
                cnt.pop(a)
            dfs(cnt, a)
            cnt[a] += 1
        return self.res