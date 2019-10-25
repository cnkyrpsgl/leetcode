class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
      parent = [0] * len(edges)

      def find(x):
        if parent[x] == 0:
          return x
        parent[x] = find(parent[x])
        return parent[x]

      def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
          return False
        parent[rootX] = rootY
        return True
      
      res = [0, 0]
      for x, y in edges:
        if not union(x - 1, y - 1): 
          res =  [x, y]
      return res