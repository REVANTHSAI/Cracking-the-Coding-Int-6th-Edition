#Delete Middle Node: Implement an algorithm to delete a node in the middle
#(i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list,
#given only access to that node.
# Assumption -  Only the node to be deleted is available
def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next
