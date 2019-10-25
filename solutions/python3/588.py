class File:
    
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = File('/')

    def move(self, path):
        cur = self.root
        if path[1:]:
            for dr in path[1:].split('/'):
                if dr not in cur.files:
                    cur.files[dr] = File(dr)
                cur = cur.files[dr]
        return cur
    
    def ls(self, path: str) -> List[str]:
        cur = self.move(path)
        return [cur.name] if cur.content else sorted(cur.files.keys())

    def mkdir(self, path: str) -> None:
        self.move(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.move(filePath)
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.move(filePath).content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)