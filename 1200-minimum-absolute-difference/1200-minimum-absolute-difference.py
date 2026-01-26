class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        if n < 2:
            return []

        arr = sorted(arr)
        min_diff = float("inf")

        res = []
        for i in range(1,n):
            diff = arr[i] - arr[i - 1]
            pair = [arr[i - 1], arr[i]]

            if diff == min_diff:
                res.append(pair)
            elif diff < min_diff:
                min_diff = diff
                res = [pair]

        return res