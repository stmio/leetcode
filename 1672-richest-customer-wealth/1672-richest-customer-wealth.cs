public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int wealth = 0;
        for (int i = 0; i < accounts.Length; i++) {
            int total = 0;
            for (int j = 0; j < accounts[i].Length; j++) {
                total += accounts[i][j];
            }
            if (total > wealth) wealth = total;
        }
        return wealth;
    }
}