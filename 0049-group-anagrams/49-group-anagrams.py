class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorts = {}

        for s in strs:
            x = "".join(sorted(s))
            sorts[x] = sorts.get(x, []) + [s]

        return list(sorts.values())