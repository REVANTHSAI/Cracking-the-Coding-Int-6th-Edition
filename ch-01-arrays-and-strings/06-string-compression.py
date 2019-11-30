# Time Complexity O(N)
import unittest
from collections import OrderedDict
def string_compression(string):
    compressed = []
    counter = 0
# Parses string and compares the consecutive charecters.
    for i in range(len(string)):
        counter += 1
# Appends count when string sequence changes or at the end of the string
        if i+1 >= len(string) or string[i] != string[i+1]:
            compressed.append(string[i]+str(counter))
            counter = 0
# Compares compressed string with the original string and returns the shorter string
    return min(string,''.join(compressed),key=len)



class test(unittest.TestCase):
    test_cases = (('aaaaaabbbbccd','a6b4c2d1'),('AAbbbbCCCd','A2b4C3d1'),('aabcccccaaa','a2b1c5a3'),('revanth','revanth'),('TestFirst','TestFirst'),('TestSecond','TestSecond'))

    def test_main(self):
        for [test,result] in self.test_cases:
            val = string_compression(test)
            self.assertEquals(val,result)


if __name__ == '__main__':
    unittest.main()
