class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                break
        else:
            return False 

        i = mid
        
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

        