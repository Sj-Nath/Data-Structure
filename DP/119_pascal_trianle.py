class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        row = [1]
        
        # Generate rows up to rowIndex
        for r in range(1, rowIndex + 1):
            new_row = [1] * (r + 1)
            for i in range(1, r):
                new_row[i] = row[i - 1] + row[i]
            row = new_row  # Update the row
        
        return row

x = Solution()
print(x.getRow(5))
