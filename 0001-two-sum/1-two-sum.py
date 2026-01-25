class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = { target - nums[i]: i for i in range(len(nums)) }
        
        for i in range(len(nums)):
            if nums[i] in x and x.get(nums[i]) != i:
                return [i, x.get(nums[i])]