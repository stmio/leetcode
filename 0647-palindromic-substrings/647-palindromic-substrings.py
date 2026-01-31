class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        c = 0

        for i in range(2 * n - 1):
            l = i // 2
            r = l + i % 2

            while 0 <= l <= r < n and s[l] == s[r]:
                c += 1
                r += 1
                l -= 1

        return c
