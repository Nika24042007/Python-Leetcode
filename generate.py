class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            row = [0]*(i+1)
            if i == 0:
                row[0] = 1
                rows.append(row)
            elif i == 1:
                row[0] = 1
                row[-1] = 1
                rows.append(row)
            else:
                for j in range(i+1):
                    if j == 0 or j == i:
                        row[j] = 1
                    else:
                        row[j] = rows[i-1][j-1] + rows[i-1][j]
                rows.append(row)
        return rows