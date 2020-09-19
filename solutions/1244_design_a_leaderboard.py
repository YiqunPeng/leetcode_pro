class Leaderboard:

    def __init__(self):
        self.player_scores = collections.defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
    	"""Running time: O(1).
    	"""
        self.player_scores[playerId] += score
        
    def top(self, K: int) -> int:
    	"""Running time: O(nlogn) where n is the size of player_scores.
    	"""
        return sum(sorted(self.player_scores.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
    	"""Running time: O(1).
    	"""
        self.player_scores[playerId] = 0