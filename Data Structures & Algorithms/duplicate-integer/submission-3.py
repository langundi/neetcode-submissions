class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()

        for i, n in enumerate(nums):
            if n in nums_set:
                return True
            else:
                nums_set.add(n)
        return False
