class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0

        while l < r:
            bound = min(height[l], height[r])
            area = (r - l) * bound
            if area > best:
                best = area
                
            if height[l] == height[r]:
                l += 1
                r -= 1
            elif bound == height[l]:
                l += 1
            else:
                r -= 1
        
        return best
