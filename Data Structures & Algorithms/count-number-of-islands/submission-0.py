class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        rows = len(grid)
        columns = len(grid[0])

        def dfs(c, r):
            print(c, r)
            if c < 0 or c >= columns or r < 0 or r >= rows:
                return

            if grid[r][c] == "0" or (c, r) in visited:
                return
                
            visited.add((c, r))

            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for dc, dr in directions:
                dfs(c + dc, r + dr)

        for c in range(columns):
            for r in range(rows):
                if (c, r) not in visited and grid[r][c] == "1":
                    islands += 1
                    dfs(c, r)

        return islands