class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        if numRows == 1:
            return ans
        ans.append([1,1])
        if numRows == 2:
            return ans
        ans.append([1,2,1])    
        if numRows == 3:
            return ans

        for i in range(2,numRows-1):
            row = [1]
            for j in range(1,len(ans[i]) // 2 + 1):
                ele = ans[i][j] + ans[i][j-1]
                row.append(ele)
            if i%2 == 0:
                row += row[::-1]
            else:
                row += row[:len(ans[i])//2][::-1]
            ans.append(row)

        return ans