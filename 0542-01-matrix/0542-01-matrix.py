class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0: q.append((r, c, 0))
                else: mat[r][c] = None
        directions = [0, 1, 0, -1, 0]
        while q:
            r, c, dis = q.popleft()
            for i in range(4):
                x, y = r + directions[i], c + directions[i + 1]

                if 0 <= x < rows and 0 <= y < cols and mat[x][y] is None:
                    mat[x][y] = dis + 1
                    q.append((x, y, dis + 1))
        return mat