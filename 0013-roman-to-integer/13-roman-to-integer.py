class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        for idx, c in enumerate(s):
            if c == "I":
                if idx < len(s) - 1 and (s[idx + 1] == "X" or s[idx + 1] == "V"):
                    total -= 1
                else:
                    total += 1
            elif c == "V":
                total += 5
            elif c == "X":
                if idx < len(s) - 1 and (s[idx + 1] == "L" or s[idx + 1] == "C"):
                    total -= 10
                else:
                    total += 10
            elif c == "L":
                total += 50
            elif c == "C":
                if idx < len(s) - 1 and (s[idx + 1] == "D" or s[idx + 1] == "M"):
                    total -= 100
                else:
                    total += 100
            elif c == "D":
                total += 500
            elif c == "M":
                total += 1000

        return total
