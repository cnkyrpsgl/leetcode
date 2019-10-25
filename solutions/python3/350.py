class Solution:
    intersect = lambda *x: [k for k, v in (collections.Counter(x[1]) & collections.Counter(x[2])).items() for _ in range(v)]