class FileSystem:

    def __init__(self):
        self.d = {"" : -1}

    def create(self, path: str, value: int) -> bool:
        parent = path[:path.rfind('/')]
        if parent in self.d and path not in self.d:
            self.d[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        return self.d.get(path, -1)