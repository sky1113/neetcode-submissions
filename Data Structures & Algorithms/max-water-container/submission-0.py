class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1

        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if area > max_area:
                max_area = area
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            
        return max_area


