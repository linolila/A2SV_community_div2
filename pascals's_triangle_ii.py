class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev_row = [1]
        for i in range(1, rowIndex + 1):
            current_row = [1]
            for j in range(1, i):
                current_row.append(prev_row[j-1] + prev_row[j])
            current_row.append(1)
            prev_row = current_row
        
        return prev_row
