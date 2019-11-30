import unittest
#Is s1 a rotated version of s2
def is_rotated_string(s1,s2):
    if (len(s1) != len(s2)) or (len(s1)==0 or len(s1)==0):
        return False
    if is_substring(s1,s2+s2):
        return True
    else:
        return False

# Return True if s1 is a substing of s2
def is_substring(s1,s2):
    if s1 in s2:
        return True
    else:
        return False


#Unit Test
class Test(unittest.TestCase):
    test_case_true = (('revanth','threvan'),('abcdefgh','fghabcde'))
    test_case_false = (('djfdsj','djfdf'),('avavde','eeeeee'))

    def test_pos_case(self):
        for test in self.test_case_true:
            result = is_rotated_string(*test)
            self.assertTrue(result)

    def test_neg_case(self):
        for test in self.test_case_false:
            result = is_rotated_string(*test)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
