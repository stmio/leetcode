class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 0:
            return ""

        bl, br = 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(n):
            o = expand(i, i)
            e = expand(i - 1, i)

            if o > br - bl + 1:
                dist = o // 2
                bl, br = i - dist, i + dist

            if e > br - bl + 1:
                dist = e // 2
                bl, br = i - dist, i + dist - 1

        return s[bl:br+1]


        