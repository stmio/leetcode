class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

        return [a[1] for a in heapq.nlargest(k, [t[::-1] for t in counts.items()])]