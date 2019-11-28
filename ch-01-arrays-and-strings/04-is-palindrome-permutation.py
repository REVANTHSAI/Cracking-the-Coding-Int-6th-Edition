import unittest
def is_permutation_of_palindrome(s1):
    char_count = {}
    odd_char_count = 0

    for char in s1:
        # Check is the charecter is between a to z or A to Z.Exclude all other charecters from count
        if is_valied_char(char):
        # Increment charecter count
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

            if char_count[char]%2 == 0:
                odd_char_count -= 1
            else:
                odd_char_count += 1

    return odd_char_count <= 1



def is_valied_char(c):

    if 'a' <= c.lower() <= 'z':
        return True
    else:
        return False


class Test(unittest.TestCase):
    dataT = ('redd er','mad am','redi vider')
    dataF = ('rev anth','pikka choo','cyber truck')

    def test_permutation(self):
        for testTrue in self.dataT:
            result = is_permutation_of_palindrome(testTrue)
            self.assertTrue(result)

        for testFalse in self.dataF:
            result = is_permutation_of_palindrome(testFalse)
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
