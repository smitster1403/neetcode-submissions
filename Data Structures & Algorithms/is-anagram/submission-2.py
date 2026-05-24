from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) > len(t)) or (len(s) < len(t)):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        if any(i not in t_counter.keys() for i in s_counter.keys()):
            return False
        
        s_items = dict(sorted(s_counter.items()))
        t_items = dict(sorted(t_counter.items()))

        return s_items == t_items

