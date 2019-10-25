class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = collections.Counter(barcodes).most_common()[::-1]
        ref = [val for val, t in cnt for _ in range(t)]
        for i in range(0, len(barcodes), 2):
            barcodes[i] = ref.pop()
        for i in range(1, len(barcodes), 2):
            barcodes[i] = ref.pop()
        return barcodes