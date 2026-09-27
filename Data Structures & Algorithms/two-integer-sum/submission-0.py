class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            map[n] = i

        for i, n in enumerate(nums):
            x = target - n
            if x in map and map[x] != i:
                return[i, map[x]]
        return []
        