class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2

        if len(nums) == 0:
            return -1

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            x = self.search(nums[mid+1:], target)
            return -1 if x == -1 else x + mid + 1

        return self.search(nums[:mid], target)                
