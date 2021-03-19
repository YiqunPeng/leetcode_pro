class FileSystem:

    def __init__(self):
        self.p = {'': None}
        
    def createPath(self, path: str, value: int) -> bool:
        if path in self.p:
            return False
        i = path.rfind('/')
        if path[:i] not in self.p:
            return False
        self.p[path] = value
        return True
        
    def get(self, path: str) -> int:
        return self.p[path] if path in self.p else -1
