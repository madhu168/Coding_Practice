class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix) # no of rows
        m = len(matrix[0]) # no of coloumns

        top = 0
        left = 0
        bottom = n - 1
        right = m - 1

        # Define ans array to store the result.
        ans = []

        while( top <= bottom and left <= right):
            
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1
            
            
            for j in range(top,bottom+1):
                ans.append(matrix[j][right])
            
            right -= 1
            
            if top <= bottom:
                for k in range(right,left-1,-1):
                    ans.append(matrix[bottom][k])
                    
                bottom -= 1
            
            if left <= right:
                for l in range(bottom,top-1,-1):
                    ans.append(matrix[l][left])
                left += 1
            
        return ans