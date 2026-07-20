class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = min(heights[l], heights[r]) * (r - l)
        while l < r:
            if min(heights[l], heights[r]) * (r - l) > maxArea:
                maxArea = min(heights[l], heights[r]) * (r - l)
            if heights[l] > heights[r]:
                r = r - 1
            else: 
                l = l + 1
        return maxArea
        