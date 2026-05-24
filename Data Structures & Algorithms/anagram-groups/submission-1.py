from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        new_strs = [''.join(sorted(x)) for x in strs]
        new_strs.sort()
        keys = Counter(new_strs).keys()
        output = []
        for k in keys:
            t = []
            for s in strs:
                if k == ''.join(sorted(s)):
                    t.append(s)
            output.append(t)

        return output
