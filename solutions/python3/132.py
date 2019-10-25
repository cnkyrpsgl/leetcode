class Solution:
    def minCut(self, s):
        q, pal, used = [(0, 0)], collections.defaultdict(list), {(0, 0)}
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]: pal[i].append(j + 1)
        while q:
            cuts, i = heapq.heappop(q)
            i *= -1
            if i == len(s): return cuts - 1
            for j in pal[i]:
                if (cuts + 1, -j) not in used:
                    used.add((cuts + 1, -j))
                    heapq.heappush(q, (cuts + 1, -j))