class Solution:
    def wordPatternMatch(self, pattern, s):
        m, n = len(pattern), len(s)
        def dfs(i, j, dic, used):
            if i >= m or j >= n:
                return i == m and j == n
            elif pattern[i] in dic:
                return s[j:j + len(dic[pattern[i]])] == dic[pattern[i]] and dfs(i + 1, j + len(dic[pattern[i]]), dic, used)
            else:
                for k in range(j + 1, n + 1):
                    if s[j:k] not in used:
                        dic[pattern[i]] = s[j:k]
                        if dfs(i + 1, j + len(dic[pattern[i]]), dic, used | {s[j:k]}):
                            return True
                        dic.pop(pattern[i])
                return False
        return dfs(0, 0, {}, set())