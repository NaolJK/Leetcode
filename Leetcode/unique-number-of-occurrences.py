class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)

        s1 = len(count.values())
        s2 = len(set(count.values()))

        return s1 == s2
        