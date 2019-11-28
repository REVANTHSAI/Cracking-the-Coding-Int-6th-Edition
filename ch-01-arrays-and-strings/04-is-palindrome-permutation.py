# Time Complexity O(N)
import unittest
def is_permutation_of_palindrome(s1):
    '''Return True if a given string is a permutation of a palindrome '''
    char_count = {}
    odd_char_count = 0

    for char in s1:
        # Check is the charecter is between a to z or A to Z. Excludes all other charecters from count
        if is_valied_char(char):
        # Increment charecter count
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        # Count the number of odd charecter count.
            if char_count[char]%2 == 0:
                odd_char_count -= 1
            else:
                odd_char_count += 1
    # If the odd charecter count is > 1, It means the given string is not a permutation of palindrome
    return odd_char_count <= 1



def is_valied_char(c):
    '''Return True if a charecter is between [a,z] or [A,A]'''
# Check of the charecter is between a to Z
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
