class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """String.

        Running time: O(n) where n is the length of typed.
        """
        def get_groups(s):
            groups = []
            c = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    c += 1
                else:
                    groups.append((s[i - 1], c))
                    c = 1
            return groups
        
        n_groups = get_groups(name)
        t_groups = get_groups(typed)
        
        if len(n_groups) != len(t_groups):
            return False
            
        return all(n_groups[i][0] == t_groups[i][0] and n_groups[i][1] <= t_groups[i][1] for i in range(len(t_groups)))
