class Solution:
# @return a list of integers
    def getRow(self, rowIndex):
        rowIndexCopy = rowIndex
        if (rowIndex == 0):
            return [1]

        else:
            final_row = [1]

            while rowIndexCopy > 0:
                final_row = self.generateNext(final_row)
                rowIndexCopy -= 1

            return final_row

    def generateNext(self, row):
        i = 0
        j = i + 1
        new_row = [1]

        while (j < len(row)):
            new_row.append(row[i] + row[j])
            i += 1
            j += 1
            new_row.append(1)

        return new_row
        
