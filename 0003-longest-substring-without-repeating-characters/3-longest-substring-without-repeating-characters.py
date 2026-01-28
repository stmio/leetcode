class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        best = 0
        left = 0

        for idx, i in enumerate(s):
            if i in seen and seen[i] >= left:
                left = seen[i] + 1
            
            seen[i] = idx
            best = max(best, idx - left + 1)

        return best
