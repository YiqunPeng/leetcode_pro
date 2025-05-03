class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        res = 0
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        while players and trainers:
            if players[-1] <= trainers[-1]:
                res += 1
                players.pop()
                trainers.pop()
            elif trainers:
                trainers.pop()
        return res