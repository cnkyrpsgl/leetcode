class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return None
        N,M=len(grid),len(grid[0])
        
        def around(r,c,t=None):
            # all cells 1-step away from (r,c)
            # optionally, if t!=None, target value must be t
            for d in (-1,1):
                for (rr,cc) in ((r+d,c), (r,c+d)):
                    if 0<=rr<N and 0<=cc<M and (t == None or grid[rr][cc]==t):
                        yield (rr,cc)
        
        def regions():
            regs=[]
            seen=set()
            for r in range(N):
                for c in range(M):
                    if grid[r][c]==1 and (r,c) not in seen:
                        # this is a new region. do a BFS to find all contiguous ones
                        reg=set()
                        front, newfront=[(r,c)], []
                        while front:
                            reg.update(front)
                            while front:
                                (r,c) = front.pop()
                                for (rr,cc) in around(r,c,1):
                                    if (rr, cc) not in reg:
                                        newfront.append((rr,cc))
                                        reg.add((rr, cc))
                            front,newfront=newfront,front
                        regs.append(reg)
                        seen.update(reg)
            return regs
        
        def reg_boundary(reg):
            # cells that would become infected by cells in reg
            bound=set()
            for (r,c) in reg:
                for (rr,cc) in around(r,c,0):
                    bound.add((rr,cc))

            return bound
        
        def reg_walls(reg,bound):
            # number of walls that would need to be built to contain reg
            walls=0
            for (r,c) in bound:
                for (rr,cc) in around(r,c,1):
                    if (rr,cc) in reg:
                        walls+=1    
            return walls
        gwalls=0
        
        while True:
            
            regs=regions()
            
            if not regs: break
            reg = max(regs, key=lambda reg: len(reg_boundary(reg)))
            walls=reg_walls(reg, reg_boundary(reg))
            gwalls+=walls
            
            # neutralize region
            for (r,c) in reg:
                grid[r][c]=2

            # compute next grid iteration after new infections
            infected=set()
            for r in range(N):
                for c in range(M):
                    if grid[r][c]==1:
                        for (rr, cc) in around(r, c, 0):
                            infected.add((rr, cc))

            for r, c in infected:
                grid[r][c]=1

            if not infected: break

        return gwalls