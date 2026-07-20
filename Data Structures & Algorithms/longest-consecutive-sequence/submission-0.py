from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecs = set(nums)
        longest = 0
        for num in nums:
            if (num - 1 not in consecs):
                length = 1
                while (num + length) in consecs:
                    length += 1
                longest = max(longest, length)
        return longest
        