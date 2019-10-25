class TopVotedCandidate:

    def __init__(self, persons, times):
        votes = collections.defaultdict(int)
        winner = 0
        self.winners = [None] * len(times)
        self.times = times
        for i, person in enumerate(persons):
            votes[person] += 1 
            if votes[person] >= votes[winner]:
                winner = person
            self.winners[i] = winner

    def q(self, t):
        return self.winners[bisect.bisect(self.times, t) - 1]