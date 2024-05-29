class Solution:
    def findMaxInRow(self, mat: List[List[int]], n: int, m: int, col: int) -> int:
        maxVal = float('-inf')
        maxValIndex = 0
        for i in range(n):
            if mat[i][col] > maxVal:
                maxVal = mat[i][col]
                maxValIndex = i
        return maxValIndex

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m-1
        while low <= high:
            mid = (low+high) // 2
            maxRowIndex = self.findMaxInRow(mat,n,m,mid)
            left = -1
            if mid-1 >= 0:
                left = mat[maxRowIndex][mid-1]
            right = -1
            if mid+1 < m:
                right = mat[maxRowIndex][mid+1]
            if mat[maxRowIndex][mid] > left and mat[maxRowIndex][mid] > right:
                return [maxRowIndex,mid]
            elif mat[maxRowIndex][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1,-1]