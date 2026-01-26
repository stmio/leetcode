class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starts = {n for n in nums if n - 1 not in nums}
        longest = 0
        
        for n in starts:
            c = 1
            while n + c in nums:
                c += 1
    
            if c > longest:
                longest = c

        return longest          