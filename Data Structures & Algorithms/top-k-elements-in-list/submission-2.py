from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = list(Counter(nums).items())

        counter.sort(key=lambda x: x[1], reverse=True)
        counter = counter[:k]

        return [a for a,b in counter]

