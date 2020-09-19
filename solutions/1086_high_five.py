class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        """Hash table.

        Running time: O(nlogn) where n is the length of items.
        """
        score_map = {}
        for i, s in items:
            self._insert_score(i, s, score_map)
        res = [[k, sum(v) // len(v)] for k, v in score_map.items()]
        return sorted(res, key=lambda x: x[0])
        
    def _insert_score(self, i, s, score_map):
        """Heap.

        Running time: O(logn) where n is the length of score_map[i].
        """
        if i not in score_map:
            score_map[i] = [s]
        elif len(score_map[i]) < 5:
            heapq.heappush(score_map[i], s)
        elif score_map[i][0] < s:
            heapq.heappushpop(score_map[i], s)
