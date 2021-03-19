class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        """Hash table.
        """
        foods = set()
        tables = {}
        for order in orders:
            t, f = int(order[1]), order[2]
            if t not in tables:
                tables[t] = {f: 1}
            else:
                tables[t][f] = tables[t].get(f, 0) + 1
            foods.add(f)
        res = []
        sfoods = sorted(list(foods))
        header = ['Table'] + [f for f in sfoods]
        res.append(header)
        for k in sorted(tables):
            row = [str(k)]
            for i in range(1, len(header)):
                row.append(str(tables[k].get(header[i], 0)))
            res.append(row)
        return res
