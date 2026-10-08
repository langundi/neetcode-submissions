class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for i, n in enumerate(strs):
            strsort = "".join(sorted(n))
            group[strsort].append(n)

        return list(group.values())