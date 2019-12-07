# Time Complexity O(N^2)
# Assumptions - Duplicates should be romoved without using any additional DS
import unittest
from linked_list import linked_list

def remove_dups_from_LL(ll):
    if ll.head == None:
        return
    iter_pointer = ll.head
    while(iter_pointer != None):
        runner_pointer =  iter_pointer
        while(runner_pointer.next != None):
            if iter_pointer.value == runner_pointer.next.value:
                runner_pointer.next = runner_pointer.next.next
            else:
                runner_pointer = runner_pointer.next
        iter_pointer = iter_pointer.next
    return ll


class Test(unittest.TestCase):
    test_case = [((1,2,4,7,8,1,6,7,1,7,8,8),(1,2,4,7,8,6)),((2,4,4,91,81,91,99,0,0),(2,4,91,81,99,0)),((1,2,2,3,3,3,4,4,5,5),(1,2,3,4,5))]

    def test_main(self):
        for (test,result) in self.test_case:
            ll = linked_list()
            ll.insert_multiple(list(test))
            value = remove_dups_from_LL(ll)
            expected_result = linked_list().insert_multiple(list(result))
            print(str(test),str(value))
            self.assertTrue(str(value),str(expected_result))

if __name__ == "__main__":
    unittest.main()
