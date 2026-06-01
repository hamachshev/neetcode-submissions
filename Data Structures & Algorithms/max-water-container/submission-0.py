class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        max_water = 0 

        while left < right:
            shorter = min(heights[left], heights[right])
            area = (right - left) * shorter
            max_water = max(max_water, area)

            if shorter == heights[left]:
                left += 1
            else:
                right -=1
        return max_water
