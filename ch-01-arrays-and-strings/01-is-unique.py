# Determine whether or not a given string contains no duplicate characters.
import unittest
def contains_no_duplicates(string):
# Assuming that string is of ASCII standard
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for letter in string:
        unicode_int = ord(letter)
        if char_set[unicode_int]:
            return False
        char_set[unicode_int] = True
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = contains_no_duplicates(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = contains_no_duplicates(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
