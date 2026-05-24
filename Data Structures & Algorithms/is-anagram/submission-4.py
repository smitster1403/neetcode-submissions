from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = Counter(s).items()
        t_c = Counter(t).items()
        return s_c == t_c