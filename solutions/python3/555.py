class Solution:
    def splitLoopedString(self, strs):
        arr, res = [s > s[::-1] and s or s[::-1] for s in strs], ""
        for i, word in enumerate(strs):
            for w in (word, word[::-1]):
                s, ind = "", 0
                for j in range(len(w)):
                    if not s or w[j:] + w[:j] > s: s, ind = w[j:] + w[:j], j   
                cur = w[ind:] + "".join(arr[i + 1:]) + "".join(arr[:i]) + w[:ind]
                if not res or cur > res: res = cur
        return res