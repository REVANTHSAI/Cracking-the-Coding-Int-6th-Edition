import unittest

def rotate_matrix(mat,rotate_clock_wise = True):

    if len(mat) == 0 or (len(mat) != len(mat[0])):
        print('Not a valid matrix')
        return

    if rotate_clock_wise:
        return matrix_mirror_image(tranpose_matrix(mat))
    else:
        return tranpose_matrix(matrix_mirror_image(mat))



def rotate_matrix_counter_clockwise(mat):
    if len(mat) == 0 or (len(mat) != len(mat[0])):
        print('Not a valid matrix')
        return

    return tranpose_matrix(matrix_mirror_image(mat))


def tranpose_matrix(mat):
    for i in range(len(mat[0])):
        for j in range(i,len(mat)):
            if j == i:
                continue
            temp = mat[j][i]
            mat[j][i] = mat[i][j]
            mat[i][j] = temp
    return mat

def matrix_mirror_image(mat):
    for i in range(len(mat)):
        mat[i].reverse()
    return mat

class Test(unittest.TestCase):
    # Test case for clock wise
    test_case_c=([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],[[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])
    # Test case for anti clock wise rotation
    test_case_ac=([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],[[4,8,12,16],[3,7,11,15],[2,6,10,14],[1,5,9,13]]
)

    def test_clockwise(self):
        (test,result) = self.test_case_c
        val = rotate_matrix(test)
        self.assertEquals(val,result)

    def test_counter_clockwise(self):
        (test,result) = self.test_case_ac
        val = rotate_matrix(test,False)
        self.assertEquals(val,result)

if __name__ == '__main__':
    unittest.main()
