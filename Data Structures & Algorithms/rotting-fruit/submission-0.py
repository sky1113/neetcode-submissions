class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        queue = deque()
        layer = deque()
        result = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append([row, col])
        
        while queue:
            print(queue)

            for _ in range(len(queue)):
                curr = queue.popleft()
                for dr, dc in directions:
                    r = curr[0] + dr
                    c = curr[1] + dc
                    if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0:
                        continue
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append([r, c])
            if queue:
                result += 1
        
        for row in grid:
            if 1 in row:
                return -1
        
        return result
                
        
