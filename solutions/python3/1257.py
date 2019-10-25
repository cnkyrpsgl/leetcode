class Solution:
    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        nex = {r: region[0] for region in regions for r in region[1:]}
        r1, r2 = region1, region2
        while r1 != r2:
            r1 = nex[r1] if r1 in nex else region2
            r2 = nex[r2] if r2 in nex else region1
        return r1
