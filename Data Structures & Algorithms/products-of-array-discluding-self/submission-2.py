import math

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out = []

        for i in range(len(nums)):
            t = nums[:i] + nums[i+1:]
            v = math.prod(t)
            out.append(v)

        return out