class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []

        for i, n in enumerate(nums):
            if n in arr:
                return True
            arr.append(n)
        return False
