class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.insert(0, 1)
        vFences.insert(0, 1)
        hFences.append(m)
        vFences.append(n)

        def f(a): 
            return {abs(a[y] - a[x]) for x in range(len(a)) for y in range(x + 1, len(a))}

        length = max(f(hFences).intersection(f(vFences)), default = 0)
        return (length ** 2) % (10**9 + 7) if length != 0 else -1
        