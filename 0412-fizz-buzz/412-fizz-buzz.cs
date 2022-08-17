public class Solution {
    public IList<string> FizzBuzz(int n) {
        string[] answer = new string[n];
        for (int i = 1; i <= n; i++) {
            answer[i-1] = (i % 3, i % 5) switch {
                (0, 0) => "FizzBuzz",
                (0, _) => "Fizz",
                (_, 0) => "Buzz",
                (_, _) => i.ToString()
            };
        }
        return answer;
    }
}