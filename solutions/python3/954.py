class Solution:
    def canReorderDoubled(self, A):
        cnt = collections.Counter(A)
        for a in sorted(A, key = abs):
            if cnt[a] and cnt[a * 2]:
                cnt[a] -= 1
                cnt[a * 2] -= 1
            elif cnt[a] and a % 2 == 0 and cnt[a // 2]:
                cnt[a] -= 1
                cnt[a // 2] -= 1   
        return all(cnt[a] == 0 for a in A)