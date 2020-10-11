class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
    	"""Sort.

    	Running time: O(n) where n is the length of restaurants.
    	"""
        candid = []
        for r in restaurants:
            i, rating, v, p, d = r
            if (not veganFriendly or v) and (p <= maxPrice) and (d <= maxDistance):
                candid.append(r)
        candid.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return [c[0] for c in candid]
