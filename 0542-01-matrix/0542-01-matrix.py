from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        queue = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float("inf")

        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                distance = mat[r][c] + 1
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] > distance:
                    queue.append((nr, nc))
                    mat[nr][nc] = distance

        return mat