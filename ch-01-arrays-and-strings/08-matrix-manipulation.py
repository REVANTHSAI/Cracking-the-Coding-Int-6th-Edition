# Space Complexity - O(1)
# Time Complexity - O(M*N)

import unittest

def manipulate_matrix(mat):
    num_of_columns = len(mat[0])
    num_of_rows = len(mat)

    # Check if first row contains a zero.
    is_zero_in_first_row = True if (0 in mat[0]) else False

    # Check if first column contains a zero.
    is_zero_in_first_column = False
    for i in range(num_of_rows):
        if mat[i][0] == 0:
            is_zero_in_first_column = True
            break

    # First row and column values will be set to zero if that particular row or column has a zero.
    for i in range(1,num_of_columns):
        for j in range(1,num_of_rows):
            if mat[i][j] == 0:
                mat[0][j] = 0
                mat[i][0] = 0

    # All the row and columns with first row or column as zero will be zet to zero
    for j in range(num_of_columns):
        if mat[0][j] == 0:
            null_matrix_columns(mat,j)

    for i in range(num_of_rows):
        if mat[i][0] == 0:
            null_matrix_rows(mat,i)

    # Set First
    if is_zero_in_first_column : null_matrix_columns(mat,0)
    if is_zero_in_first_row : null_matrix_rows(mat,0)

    return mat

#Sets column values to zero for a given column_no
def null_matrix_columns(mat,column_no):
    for i in range(len(mat)):
        mat[i][column_no] = 0
    return

#Sets row values to zero for a given row_no
def null_matrix_rows(mat,row_no):
    mat[row_no] = [0]*len(mat[0])
    return


# Tests
class Test(unittest.TestCase):
    test_case1 =([[1,2,3,4,5],[1,0,1,1,6],[1,2,4,5,7],[2,1,5,0,8],[2,3,4,5,9]],[[1,0,3,0,5],[0,0,0,0,0],[1,0,4,0,7],[0,0,0,0,0],[2,0,4,0,9]])
    test_case2 =([[1,2,3,4,5],[1,0,1,1,6],[0,2,4,5,7],[2,1,5,0,8],[2,3,4,5,9]],[[0,0,3,0,5],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,4,0,9]])

    def test_1(self):
        (test,result) = self.test_case1
        val = manipulate_matrix(test)
        self.assertEqual(val,result)

    def test_2(self):
        (test,result) = self.test_case2
        val = manipulate_matrix(test)
        self.assertEqual(val,result)


if __name__ == "__main__":
    unittest.main()
