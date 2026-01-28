class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = defaultdict(int)
        for c in s1:
            counts[c] += 1

        window_size = len(s1)

        for left in range(0, len(s2) - window_size + 1):
            window = s2[left:left + window_size]
            permutation_counts = defaultdict(int)

            for c in window:
                permutation_counts[c] += 1

            if permutation_counts == counts:
                return True

        return False
