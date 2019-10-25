class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        return min((set(fronts) | set(backs)) - set(fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]), default = 0)