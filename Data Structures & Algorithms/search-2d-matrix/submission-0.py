class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        low = 0
        high = (R * C) - 1

        while low <= high:
            mid = low + ((high - low) // 2)
            mid_r = mid // C
            mid_c = mid % C

            curr = matrix[mid_r][mid_c]

            if curr < target:
                low = mid + 1
            elif curr > target:
                high = mid - 1
            elif curr == target:
                return True

        return False
