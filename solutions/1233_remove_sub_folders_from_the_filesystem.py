class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
    	"""String.
    	"""
        folder.sort()
        res = [folder[0]]
        f = folder[0]
        for i in range(1, len(folder)):
            if folder[i][:len(f)] != f or folder[i][len(f)] != '/':
                res.append(folder[i])
                f = folder[i]
        return res
