from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counters = Counter(nums)
        x = [(l,k) for k,l in sorted([(j,i) for i,j in counters.items()], reverse=True)]
        out = [a for a,b in x ]

        return out[:k]
        