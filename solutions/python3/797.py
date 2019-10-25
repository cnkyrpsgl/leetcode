class Solution:
    def allPathsSourceTarget(self, graph, i = 0, q = [0]):
        if i == 0: 
            global res
            res = []
        if i == len(graph) - 1: 
            res.append(q)
        for index in graph[i]: 
            self.allPathsSourceTarget(graph, index, q + [index])
        return res