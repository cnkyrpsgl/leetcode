class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x,y = 0, 0
        for char in moves:
            if char=="R": x+=1
            if char=="L": x-=1
            if char=="U": y+=1
            if char=="D": y-=1
        return True if x==0 and y==0 else False
        