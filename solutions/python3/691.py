class Solution:
    def minStickers(self, stickers, target):
        cnt, res, n = collections.Counter(target), [float("inf")], len(target)  
        def dfs(dic, used, i):
            if i == n:
                res[0] = min(res[0], used)
            elif dic[target[i]] >= cnt[target[i]]:
                dfs(dic, used, i + 1)
            elif used < res[0] - 1:
                for sticker in stickers:
                    if target[i] in sticker:
                        for s in sticker:
                            dic[s] += 1
                        dfs(dic, used + 1, i + 1)
                        for s in sticker:
                            dic[s] -= 1
        dfs(collections.defaultdict(int), 0, 0)
        return res[0] < float("inf") and res[0] or -1