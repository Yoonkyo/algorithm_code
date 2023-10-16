class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[] for _ in range(rowIndex+1)]

        for i in range(0, rowIndex+1):
            for j in range(0, i+1):
                if i == 0 or j == 0 or j == i:
                    ans[i].append(1)
                else:
                    ans[i].append(ans[i-1][j-1] + ans[i-1][j])

        return(ans[rowIndex])
