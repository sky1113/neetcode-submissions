class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        num_rows = len(boxGrid)
        num_cols = len(boxGrid[0])
        
        for row in range(num_rows): # iterate through rows
            for col in range(num_cols - 1, -1, -1): # iterate from right to left
                if boxGrid[row][col] == "#": # if theres a stone, check right
                    col1 = col
                    col2 = col + 1
                    while col2 <= num_cols - 1 and boxGrid[row][col2] == ".": # check if right is valid position, then check if free
                        boxGrid[row][col2] = "#"
                        boxGrid[row][col1] = "."
                        col1 += 1
                        col2 += 1
        
        
        for row in range(num_rows):
            print(boxGrid[row])

        res = []


        for c in range(num_cols):
            col = []
            for r in range(num_rows - 1, -1, -1):
                col.append(boxGrid[r][c])
            res.append(col)

        return res