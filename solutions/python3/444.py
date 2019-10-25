class Solution:
    def sequenceReconstruction(self, org, seqs):
        order, orders, graph, seen = collections.defaultdict(int), set(), collections.defaultdict(set), set()
        for seq in seqs:
            for i in range(len(seq)):
                if i > 0:
                    if seq[i] == seq[i - 1]: return False
                    graph[seq[i - 1]].add(seq[i])
                seen.add(seq[i])
        if not seen: return False
        for i in range(len(org) - 1, -1, -1):
            if org[i] in seen: seen.discard(org[i])
            order[org[i]] = max([order[v] for v in graph[org[i]]] or [0]) + 1
            before = set(v for v in graph[org[i]] if v in seen) 
            if order[org[i]] in orders or before:
                return False
            orders.add(order[org[i]])
        return not seen