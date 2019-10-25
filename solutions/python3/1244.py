class Leaderboard:
    def __init__(self):
        self.scores = collections.defaultdict(set)
        self.p = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[self.p[playerId]].discard(playerId)
        self.p[playerId] += score
        self.scores[self.p[playerId]].add(playerId)

    def top(self, K: int) -> int:
        sm = cnt = 0
        for score, players in sorted(self.scores.items())[::-1]:
            if len(players) + cnt <= K:
                sm += len(players) * score
                cnt += len(players)
            else:
                sm += (K - cnt) * score
                cnt = K
        return sm

    def reset(self, playerId: int) -> None:
        self.scores[self.p[playerId]].discard(playerId)
        self.p[playerId] = 0
        self.scores[0].add(playerId)
