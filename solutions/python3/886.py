class Solution:
    def merge(self, node, p, group, disliked):
        group[node] = p
        for v in disliked[node]:
            if group[v] == p or (group[v] == v and not self.merge(v, -p, group, disliked)): return False
        return True
    
    def possibleBipartition(self, N, dislikes):
        group, disliked = [i for i in range(N + 1)], collections.defaultdict(set)
        for a, b in dislikes:
            disliked[a].add(b)
            disliked[b].add(a) 
        for i in range(1, N + 1):
            if group[i] == i and not self.merge(i, 2001, group, disliked): return False
        return True