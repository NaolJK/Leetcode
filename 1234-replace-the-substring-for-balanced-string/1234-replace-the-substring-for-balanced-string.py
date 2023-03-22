class Solution:
    def balancedString(self, s):
        count = collections.Counter(s)
        ans = n = len(s)
        idx = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while idx < n and all(n / 4 >= count[c] for c in 'QWER'):
                ans = min(ans, j - idx + 1)
                count[s[idx]] += 1
                idx += 1
        return ans
        