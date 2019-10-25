class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = [label]
        while label != 1:
            d = int(math.log(label) / math.log(2))
            offset = int(2 ** (d + 1)) - label - 1
            label = (int(2 ** d) + offset) // 2
            res = [label] + res
        return res