class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,3,4, 5,6,7]
        [1,2,6,24,]
        """
        n = len(nums)
        res = [1] * n

        prefix = 1
        suffix = 1

        for i in range(0, n):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
