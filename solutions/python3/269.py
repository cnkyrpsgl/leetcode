class Solution(object):
    def alienOrder(self, words):
        if len(words) == 1: return words[0]
        def dfs(i):
            visited[i] = 0
            for v in graph[i]:
                if visited[v] == 0 or (visited[v] == -1 and not dfs(v)): return False
            order.append(chr(97 + i))
            visited[i] = 1
            return True
        graph, visited, order = collections.defaultdict(set), [1] * 26, []
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[ord(c1) - ord("a")].add(ord(c2) - ord("a"))
                    break
            for c in w1 + w2: visited[ord(c) - ord("a")] = -1
        for i in range(26):
            if visited[i] == -1 and not dfs(i): return ""
        return "".join(order)[::-1]