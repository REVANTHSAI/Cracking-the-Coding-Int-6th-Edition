#Delete Middle Node: Implement an algorithm to delete a node in the middle
#(i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list,
#given only access to that node.
# Note -  Only the node to be deleted can be provided as the function parameter
from linked_list import linked_list
def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next

ll = linked_list()
ll.insert_multiple([1, 2, 3, 4])
middle_node = ll.inset_at_end(5)
ll.insert_multiple([7, 8, 9])

print(ll)2q
delete_middle_node(middle_node)
print(ll)
