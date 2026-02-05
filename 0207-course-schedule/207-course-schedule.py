class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prq = { i: [] for i in range(numCourses) }
        visited = set()
        finished = set()
        
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
            return x

        return all(dfs(i) for i in range(numCourses))