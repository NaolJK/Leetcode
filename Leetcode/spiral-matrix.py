class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        ans = []
        top = 0
        left = 0
        down = m - 1
        right = n - 1

        # Repeatedly add matrix[r1..r2][c1..c2] to ans
        while len(ans) < m * n:
            j = left
            while j <= right and len(ans) < m * n:
                ans.append(matrix[top][j])
                j += 1
            i = top + 1
            while i <= down - 1 and len(ans) < m * n:
                ans.append(matrix[i][right])
                i += 1
            j = right
            while j >= left and len(ans) < m * n:
                ans.append(matrix[down][j])
                j -= 1
            i = down - 1
            while i >= top + 1 and len(ans) < m * n:
                ans.append(matrix[i][left])
                i -= 1
            top += 1
            left += 1
            down -= 1
            right -= 1

        return ans