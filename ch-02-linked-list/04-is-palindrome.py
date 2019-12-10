#Time Complexity - O(N)
# Space Complexity - O(1)
import unittest
from linked_list import linked_list

def isPalindrome(ll):
    slow_pointer = ll.head
    fast_pointer = ll.head
    stack = []

# Move Fast ponter 2 node and slow ponter one node at a time
    while fast_pointer and fast_pointer.next:
        stack.append(slow_pointer.value)
        print(fast_pointer.value)
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

# If the LL lengths is Odd then skip the middle element
# if x and if x is not None are not the same!

    if fast_pointer:
        slow_pointer = slow_pointer.next

# Compare values in the LL to the right half of the Linked List
    while slow_pointer:
        top = stack.pop()
        if slow_pointer.value != top:
            return False
        slow_pointer = slow_pointer.next

    return True


class Test(unittest.TestCase):
    test_case_pos = ((1,2,3,4,5,4,3,2,1),('T','E','S','S','E','T'),('c','i','v','i','c'),('r','a','c','e','c','a','r'))
    test_case_neg = ((1,2,3,4,5),('r','e','v','a','n','t','h'),('s','a','i'),('p','y','t','h','o','n','i','c'))

    def test_pos(self):
        for test in self.test_case_pos:
            ll = linked_list()
            ll.insert_multiple(list(test))
            self.assertTrue(isPalindrome(ll))

    def test_neg(self):
        for test in self.test_case_neg:
            ll = linked_list()
            ll.insert_multiple(list(test))
            self.assertFalse(isPalindrome(ll))

if __name__ == "__main__":
    unittest.main()
