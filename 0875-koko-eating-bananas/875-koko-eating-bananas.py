class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ptr = l

        while l < r:
            ptr = (l + r) // 2
            s = 0

            for p in piles:
                s += math.ceil(p / ptr)

            if s > h:
                l = ptr + 1
            else:
                r = ptr

        return l
