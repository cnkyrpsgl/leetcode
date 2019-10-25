class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        st = set(folder)
        for f in folder:
            if any(p in st for p in itertools.accumulate(f.split('/'), lambda x, y: x + '/' + y) if p and p != f):
                st.discard(f)
        return list(st)   