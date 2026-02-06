class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)

        for l in magazine:
            mag[l] += 1

        for r in ransomNote:
            mag[r] -= 1

            if mag[r] < 0:
                return False

        return True