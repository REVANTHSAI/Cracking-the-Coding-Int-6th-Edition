import unittest
#Complexity O(N LogN)
def is_permutation(s1,s2):
    if (len(s1) != len(s2)):
        return False
    s1_list = [char for char in s1]
    s2_list = [char for char in s2]
    s1_list.sort()
    s2_list.sort()
#Pythons in built sort function uses time sort.
    if s1_list == s2_list:
        return True
    else:
        return False


class Test(unittest.TestCase):
    dataT = (('abcd','badc'),('3563476', '7334566'),('wef34f', 'wffe34'))
    dataF = (('abcd', 'd2cba'),('2354', '1234'),('dcw4f', 'dcw5f'))

    def test_permutation(self):
        for testTrue in self.dataT:
            result = is_permutation(*testTrue)
            self.assertTrue(result)

        for testFalse in self.dataF:
            result = is_permutation(*testFalse)
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
