class Solution:
    def rearrangeString(self, s, k):
        q, last, res, wq = [(-v, k) for k, v in collections.Counter(s).items()], {}, "", []
        heapq.heapify(q)
        for i in range(len(s)):
            if wq and (wq[0][1] not in last or last[wq[0][1]] + k <= i): cnt, char = heapq.heappop(wq)
            else:
                while q and not (q[0][1] not in last or last[q[0][1]] + k <= i): heapq.heappush(wq, heapq.heappop(q))
                if not q: return ""
                cnt, char = heapq.heappop(q)
            res, cnt, last[char] = res + char, cnt + 1, i
            if cnt: heapq.heappush(q, (cnt, char))
        return res