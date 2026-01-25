class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1
        rev = (str(abs(x)))[::-1]

        n = int(rev) * neg

        if abs(n) > 2147483648:
            return 0

        return n