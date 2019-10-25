class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m,n=len(grid),len(grid[0])

        # augment matrix to void length check
        grid.append([0]*n)
        for row in grid: row.append(0)

        self.pool=set()
        self.res=0

        def bfs(i0,j0):
            grid[i0][j0]=-1
            q=[(i0,j0)]
            for i,j in q:
                for I,J in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                    if grid[I][J]==1:
                        grid[I][J]=-1
                        q.append([I,J])
            self.addisland(q)
       
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: bfs(i,j)

        return self.res

    def addisland(self,q):
            Imin=min(x for x,y in q)
            Jmin=min(y for x,y in q)
            island1=tuple(sorted((x-Imin,y-Jmin) for x,y in q)) # original island
           
            if island1 in self.pool: return None
            self.res+=1

            Imax=max(x for x,y in island1)
            Jmax=max(y for x,y in island1)

            island2=tuple(sorted((-x+Imax,y) for x,y in island1)) # x axis mirror
            island3=tuple(sorted((x,-y+Jmax) for x,y in island1)) # y axis mirror
            island4=tuple(sorted((-x+Imax,-y+Jmax) for x,y in island1)) # origin mirror

            island5=tuple(sorted((y,x) for x,y in island1)) # diagonal mirror
            island6=tuple(sorted((-x+Jmax,y) for x,y in island5))
            island7=tuple(sorted((x,-y+Imax) for x,y in island5))
            island8=tuple(sorted((-x+Jmax,-y+Imax) for x,y in island5))

            self.pool |= set([island1,island2,island3,island4,island5,island6,island7,island8])