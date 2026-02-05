class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prq = { i: [] for i in range(numCourses) }
        visited = set()
        finished = set()
        order = []
        
        for i, j in prerequisites:
            prq[i] += [j]

        def dfs(node):
            if node in finished:
                return True
            if node in visited:
                return False

            visited.add(node)
            x = all(dfs(n) for n in prq[node])
            visited.remove(node)
            finished.add(node)
            order.append(node)
            return x

        cycle = any(not dfs(i) for i in range(numCourses))
        return [] if cycle else order