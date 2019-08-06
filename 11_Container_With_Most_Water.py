"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Moving edge from left, right to middle, if left side short, move left to middle, since short * n >= short * n - 1, or short * n >= any# * (n - 1) for any# <= short.
        
        Time: O (N)
        Space: O (1)
        """
        l = 0
        r = len(height) - 1
        
        area = 0
        while l < r:
            curArea = (r - l) * min(height[r],height[l])
            area = max(area, curArea)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return area
