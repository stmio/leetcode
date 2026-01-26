class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        x = {}

        for i in range(len(s)):
            x[s[i]] = 1 + x.get(s[i], 0)
            x[t[i]] = -1 + x.get(t[i], 0)

        return all(i == 0 for i in x.values())

