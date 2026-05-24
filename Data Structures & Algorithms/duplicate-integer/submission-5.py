from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = Counter(nums).items()

        if any(v>1 for k,v in temp):
            return True
        
        return False


        