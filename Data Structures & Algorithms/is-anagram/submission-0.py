class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        if len(s_list) == len(t_list):
            for i, n in enumerate(s_list):
                if n == t_list[i]:
                    continue
                return False
            return True
        return False