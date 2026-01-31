class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        temp = 0

        if len(nums) == 1:
            return nums[0]

        for n in nums[1:]:
            temp = prev1
            prev1 = max(prev1, prev2 + n)
            prev2 = temp

        m = prev1
        prev1 = 0
        prev2 = 0

        for n in nums[:-1]:
            temp = prev1
            prev1 = max(prev1, prev2 + n)
            prev2 = temp
        
        return max(m, prev1)
