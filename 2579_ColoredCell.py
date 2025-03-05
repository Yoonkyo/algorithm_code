class Solution:
    def coloredCells(self, n: int) -> int:
        cell = 1
        for i in range(n):
            cell += i*4
        return cell
