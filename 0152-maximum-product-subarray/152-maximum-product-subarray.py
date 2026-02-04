class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best_min = best_max = res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            if n < 0:
                best_min, best_max = best_max, best_min

            best_max = max(best_max*n, n)
            best_min = min(best_min*n, n)

            res = max(res, best_max)

        return res