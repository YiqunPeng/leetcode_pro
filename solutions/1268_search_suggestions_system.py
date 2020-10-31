class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """Binary search.

        Running time: O(nlogn) where n == len(products).
        """
        products.sort()
        pref = ''
        res = []
        i = 0
        for c in searchWord:
            pref += c
            i = bisect.bisect_left(products, pref, i)
            res.append([i for i in products[i:i+3] if i.startswith(pref)])
        return res
