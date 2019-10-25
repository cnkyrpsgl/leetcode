class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        x = (rec1[2] - rec1[0] + rec2[2] - rec2[0]) > (max(rec1[2], rec2[2]) - min(rec1[0], rec2[0]))
        y = (rec1[3] - rec1[1] + rec2[3] - rec2[1]) > (max(rec1[3], rec2[3]) - min(rec1[1], rec2[1]))
        return x and y