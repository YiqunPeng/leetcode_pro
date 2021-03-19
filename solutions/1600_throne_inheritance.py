class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingdom = {kingName: []}
        self.d = set()
        self.king_name = kingName

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.kingdom:
            self.kingdom[parentName] = [childName]
        else:
            self.kingdom[parentName].append(childName)

    def death(self, name: str) -> None:
        self.d.add(name)

    def getInheritanceOrder(self) -> List[str]:
        return self._dfs(self.king_name, [self.king_name] if self.king_name not in self.d else [])

    def _dfs(self, name, inheri):
        if name not in self.kingdom:
            return inheri
        for child in self.kingdom[name]:
            if child not in self.d:
                inheri.append(child)
            self._dfs(child, inheri)
        return inheri
