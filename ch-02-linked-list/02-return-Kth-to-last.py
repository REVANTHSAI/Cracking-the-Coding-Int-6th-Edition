import unittest
from linked_list import linked_list
# Time Complexity O(N)
def return_kth_element_from_last(ll,k):
    if ll.head == None or ll == None:
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

# Function that geneates a LL from a list
def create_from_list(list_var):
    # Initating Linked list with first element of the list as head
    ll = linked_list()
    # Appending remaing elements to the list
    for i in range(0,len(list_var)):
        ll.inset_at_end(list_var[i])
    return ll

class Test(unittest.TestCase):
    test_case = [([1,2,4,7,8,1,6,7,1,7,8,8],3,8),([2,4,4,91,81,91,99,0,0],4,91),([1,2,2,3,3,3,4,4,5,5],5,3)]

    def test_main(self):
        for (ll,k,result) in self.test_case:
            val = return_kth_element_from_last(create_from_list(ll),k)
            print("List: "+str(create_from_list(ll)),"Element From End: "+str(k),"Result: "+str(val))
            self.assertTrue(val,result)

if __name__ == "__main__":
    unittest.main()
