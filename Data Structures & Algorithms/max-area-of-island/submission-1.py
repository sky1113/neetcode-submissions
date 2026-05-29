class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        max_area = 0;
        visited = set()
        height, width = len(grid), len(grid[0])

        def dfs(r, c):
            if (r >= height or r < 0
                or c >= width or c < 0
                or grid[r][c] == 0
                or (r, c) in visited):
                return 0

            visited.add((r, c))
            curr_area = 1

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                curr_area += dfs(r + dr, c + dc)
            
            return curr_area
        
        for r in range(height):
            for c in range(width):
                if (grid[r][c] == 1 and (r, c) not in visited):
                    max_area = max(max_area, dfs(r, c))

        return max_area




