class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0] * n for _ in range(amount + 1)]
        dp[0] = [1] * n

        if amount == 0:
            return 1

        for i in range(1, amount + 1):
            for j, c in enumerate(coins):
                if i - c >= 0:
                    dp[i][j] = dp[i - c][j] 
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]
