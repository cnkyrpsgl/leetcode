class Solution:
    def predictPartyVictory(self, senate):
        ban_r = ban_d = 0
        while True:
            new = []
            r_cnt = d_cnt = 0
            for s in senate:
                if s == 'R': 
                    r_cnt += 1
                    if ban_r > 0: 
                        ban_r -= 1
                    else: 
                        ban_d += 1
                        d_cnt -= 1
                        new.append(s)
                elif s == 'D':
                    d_cnt += 1
                    if ban_d > 0: 
                        ban_d -= 1
                    else: 
                        ban_r += 1
                        r_cnt -= 1
                        new.append(s)
            if d_cnt < 0 < r_cnt:
                return "Radiant"
            elif r_cnt < 0 < d_cnt:
                return "Dire"
            senate = new