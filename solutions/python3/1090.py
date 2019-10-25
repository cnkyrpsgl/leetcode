class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        cnt = collections.defaultdict(int)
        heap = [[-a, b] for a, b in zip(values, labels)]
        heapq.heapify(heap)
        use = sm =0 
        while use < num_wanted and heap:
            a, b = heapq.heappop(heap)
            if cnt[b] < use_limit:
                sm -= a
                use += 1
                cnt[b] += 1
        return sm