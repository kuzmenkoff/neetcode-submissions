class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range (len(matrix)):
            if (target <= matrix[i][len(matrix[i])-1]):
                break
        
        left, right = 0, len(matrix[i]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[i][mid]:
                return True
            elif target > matrix[i][mid]:
                left = mid + 1
            elif target < matrix[i][mid]:
                right = mid - 1
        
        return False

        