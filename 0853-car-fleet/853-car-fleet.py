class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pairs = [(position[i], (target - position[i]) / speed[i]) for i in range(n)]
        stack = []

        pairs.sort(reverse=True)

        for _, t in pairs:
            if not stack:
                stack.append(t)
            elif t > stack[-1]:
                stack.append(t)

        return len(stack)