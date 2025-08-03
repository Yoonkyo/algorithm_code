class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        row = 0
        while row < numRows:
            row += 1
            row_list = [1]*row
            for i in range(1, row-1):
                row_list[i] = row_before[i-1] + row_before[i]
            result.append(row_list)
            row_before = row_list
        return result
