class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        ps = sorted(count.keys())
        dp = [0] * (len(ps))

        dp[0] = ps[0] * count[ps[0]]

        for i, p in enumerate(ps):
            take = p * count[p]

            j = i - 1
            while j >= 0 and ps[j] >= p - 2:
                j -= 1

            if j >= 0:
                take += dp[j]

            dp[i] = max(take, dp[i - 1])

        return dp[-1]