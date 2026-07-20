class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1

        sorted_items = sorted(d.items(), key=lambda pair: pair[1])
        return [pair[0] for pair in sorted_items[-k:]]
        