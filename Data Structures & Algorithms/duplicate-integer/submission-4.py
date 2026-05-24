from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter_nums = Counter(nums)

        return any(x > 1 for x in counter_nums.values())