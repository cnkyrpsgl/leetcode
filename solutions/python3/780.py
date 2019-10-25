class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        while sx<tx and sy<ty: tx,ty = tx%ty,ty%tx
        return sx==tx and (ty-sy)%sx==0 or sy==ty and (tx-sx)%sy==0