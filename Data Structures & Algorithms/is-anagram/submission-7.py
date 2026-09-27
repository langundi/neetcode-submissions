class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = dict.fromkeys(s, 0)
        t_map = dict.fromkeys(t, 0)

        for i, n in enumerate(s):
            s_map[n] += 1
        
        for i, n in enumerate(t):
            t_map[n] += 1

        return s_map == t_map
