class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        temp = 0
    
        for n in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + n)
            prev2 = temp

        return prev1