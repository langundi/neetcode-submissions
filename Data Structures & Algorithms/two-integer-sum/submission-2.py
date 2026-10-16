class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i == j:
                    break
                if n + m == target:
                    return [j, i]

        return []