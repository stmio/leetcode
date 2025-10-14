class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def bins(xs, t):
            if len(xs) == 0:
                return 0
            mid = len(xs) // 2
            if xs[mid] >= t:
                return bins(xs[:mid], t)
            return mid + 1 + bins(xs[(mid + 1):], t)
        tails = [nums[0]]
        for i in range(1, len(nums)):
            idx = bins(tails, nums[i])
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
        return len(tails)