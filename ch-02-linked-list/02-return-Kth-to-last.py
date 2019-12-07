import unittest
from linked_list import linked_list
# Time Complexity O(N)
def return_kth_element_from_last(ll,k):
    if ll.head == None:
        return
    f_pointer = ll.head
    s_pointer = ll.head
# Move second pointer to Kth element
    for _ in range(k-1):
        s_pointer = s_pointer.next
# Move First and second pointer simultaneously untill second pointer reaches the end of LL
    while s_pointer.next != None:
        f_pointer = f_pointer.next
        s_pointer = s_pointer.next
# When second pointer reaches the end first pointer will be at K elements from the end
    return f_pointer.value


class Test(unittest.TestCase):
    test_case = [((1,2,4,7,8,1,6,7,1,7,8,8),3,8),((2,4,4,91,81,91,99,0,0),4,91),((1,2,2,3,3,3,4,4,5,5),5,3)]

    def test_main(self):
        for (lst,k,result) in self.test_case:
            ll = linked_list()
            ll.insert_multiple(list(lst))
            val = return_kth_element_from_last(ll,k)
            print("List: "+str(ll),"Element From End: "+str(k),"Result: "+str(val))
            self.assertTrue(val,result)

if __name__ == "__main__":
    unittest.main()
