class Solution:

    def product(self, vals: List[int]) -> int:
        val = 1

        for i in vals:
            val = val * i

        return val

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        
        for i in range(len(nums)):
            t = nums[:i] + nums[i+1:]
            v = self.product(t)
            out.append(v)

        return out