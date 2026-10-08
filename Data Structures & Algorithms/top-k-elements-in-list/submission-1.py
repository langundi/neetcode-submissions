class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = defaultdict(int)

        for i, n in enumerate(nums):
            group[n] = 1 + group.get(n, 0)

        pairs = list([])
        
        for key, n in group.items():
            pairs.append([n, key])

        pairs.sort()
        result = []

        while len(result) < k:
            result.append(pairs.pop()[1])

        return result

