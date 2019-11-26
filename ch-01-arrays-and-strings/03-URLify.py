import unittest

def urlify_string(str,real_length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    # Count the number if spaces in the string
    space_count = 0
    for i in str[:real_length]:
        if i == " ":
            space_count += 1
    index = real_length + (space_count*2)


    #converting to list as python strings are Immutable.
    #Also trimming the extra spae at the end of string
    str_list = list(str[:real_length])

    # Extending the list to accomadate %20 attributes that will be inseted
    str_list.extend(["" for _ in range(space_count*2)])

    # Insert %20 at spaces
    for i in reversed(range(real_length)):
        if str_list[i] == " ":
            str_list[index-3:index] = '%20'
            ''.join(str_list)
            index -= 3
        else:
            str_list[index-1] = str_list[i]
            index -= 1

    return ''.join(str_list)




class Test(unittest.TestCase):
    test_cases = (('abcd Abdd ened   ',14,'abcd%20Abdd%20ened'),('Revanth Sai Reddy   ',17,'Revanth%20Sai%20Reddy'),('Sree xxxxx eeeee',16,'Sree%20xxxxx%20eeeee'))

    def test_URLify(self):
        for [test,real_len,result] in self.test_cases:
            val = urlify_string(test,real_len)
            self.assertEquals(val,result)



if __name__ == '__main__':
    unittest.main()
