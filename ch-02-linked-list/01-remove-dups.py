def remove_dups_from_LL(linked_list):
    iter_pointer = linked_list.Head
    runner_pointer = linked_list.Head.next

    for i in range(len(linked_list)):
        for j in range(i+1,len(linked_list)):
            if iter_pointer.value == runner_pointer.value:
                positon_of_duplicate = i+j
                delete_node(positon_of_duplicate)
            runner_pointer = runner_pointer.next
        iter_pointer = iter_pointer.next



def create_from_list(list):
    # Initating Linked list with first element of the list as head
    ll = linked_list(list[0])
    # Appending remaing elements to the list
    for i in range(1,len(list)):
        ll.inset_at_end(list[i])
