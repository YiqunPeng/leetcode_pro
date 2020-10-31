class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        """Hash set.

        Running time: O(n^2*m) where n == len(favoriteCompanies) and m = max(len(c in favoriteCompanies)).
        """
        res = []
        favoriteCompanies = [set(i) for i in favoriteCompanies]
        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if favoriteCompanies[i] < favoriteCompanies[j]:
                    break
            else:
                res.append(i)
        return res            
