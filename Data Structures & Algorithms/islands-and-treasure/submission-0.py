class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                
        while queue:
            curr = queue.pop()
            num = grid[curr[0]][curr[1]]

            for dr, dc in dirs:
                row = curr[0] + dr
                col = curr[1] + dc

                if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                    continue
                elif grid[row][col] == -1:
                    continue
                elif grid[row][col] > num + 1:
                    grid[row][col] = num + 1
                    queue.append([row, col])
                