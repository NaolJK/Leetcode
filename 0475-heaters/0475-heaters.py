class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
            
        heaters.sort()
        ans = 0
        for house in houses:

            pos = bisect_left(heaters, house)
            if pos > 0 and pos < len(heaters):
                mnm = min(abs(house - heaters[pos]), abs(house - heaters[pos-1]))

            elif pos >= len(heaters):
                mnm = abs(house - heaters[pos-1])
            else:
                mnm = abs(house - heaters[pos])

            ans = max(mnm, ans)

        return ans