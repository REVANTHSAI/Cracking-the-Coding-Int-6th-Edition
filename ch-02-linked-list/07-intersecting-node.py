#Given two single ll, determine if the two ll intersect.Return the intersecting node
#Time Complexity - O(len(ll1)+len(ll2))
import linked_list from linked_list
import unittest

def get_intersection_point(ll1,ll2):
    if not is_intersecting(ll1,ll2):
        return
    shorter = ll1 if len(ll1)<=len(ll2) else ll2
    longer =  ll2 if len(ll1)<len(ll2) else ll1
# Calculate length of LL1
    length_difference = len(longer)-len(shorter)
    longer_node,shorter_node = longer.head,shorter.head
    for _ in range(length_difference):
        longer_node = longer_node.next
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next
    return longer_node

def is_intersecting(ll1,ll2):
    temp1 = ll1.head
    temp2 = ll2.head
    if ll1.next == None or ll2.next == None:
        return False
# Get the last node of the Linked List1
    while temp1:
        temp1 = temp1.next
# Get the last node of the Linked List2
    while temp2:
        temp2 = temp2.next
# If both the LL have the same last node, Both the LL have an intersection point
    if temp1 == temp2:
        return True
    return False
