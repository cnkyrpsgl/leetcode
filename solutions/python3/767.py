class Solution:
    def reorganizeString(self, S):
        cnt, res = collections.Counter(S), ""
        while len(res) < len(S):
            c, i = cnt.most_common()[0], 0
            while i + 1 < len(cnt) and (res and res[-1] == c[0] or cnt[c[0]] == 0): c, i = cnt.most_common()[i + 1], i + 1
            if not cnt[c[0]] or res and res[-1] == c[0]: return ""
            else: res, cnt[c[0]] = res + c[0], cnt[c[0]] - 1
        return res