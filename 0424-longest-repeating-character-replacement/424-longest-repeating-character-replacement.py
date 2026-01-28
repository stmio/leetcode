class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chars = set(s)

        for x in chars:
            l = 0
            count = 0

            for r, c in enumerate(s):
                if c == x:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == x:
                        count -= 1
                    l += 1

                res = max(res,r-l+1)

        return res

                
