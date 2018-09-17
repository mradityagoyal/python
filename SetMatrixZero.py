class SetMatrixZero(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        numRows = len(matrix)
        numCols = len(matrix[0])
        for col in range(0, numCols):
            for row in range(0, numRows):
                if matrix[row][col] == 0:
                    #that row.
                    for k in range(0, numCols):
                        if matrix[row][k] != 0: matrix[row][k]= '*'
                    #that col
                    for k in range(0, numRows):
                        if matrix[k][col] != 0: matrix[k][col]= '*'

        for col in range(0, numCols):
            for row in range(0, numRows):
                if matrix[row][col] == '*': matrix[row][col] = 0
        return matrix

#
sm = SetMatrixZero()
res = sm.setZeroes([[1,1,1],
              [1,0,1],
              [1,1,1]])
for r in res: print(r)

for r in sm.setZeroes([
                          [0,1,2,0],
                          [3,4,5,2],
                          [1,3,1,5]
                      ]): print(r)