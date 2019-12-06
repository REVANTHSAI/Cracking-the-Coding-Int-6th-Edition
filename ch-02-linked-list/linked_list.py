class node():

    def __init__(self,vlaue):
        self.value  = vlaue
        self.next = None


class linked_list():
    def __init__(self):
        self.head = None

# Make the linked_list Iterable
    def __iter__(self):
        temp = self.head
        if temp == None: yield temp
        while temp != None:
            yield temp.value
            temp = temp.next

    # Overload Length operator
    def __len__(self):
        result = 0
        for _ in self:
            result+=1
        return result

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)


    def generator(self,n,min_value,max_value):
        for _ in range(n):
             self.inset_at_end(random.randint(min_value,max_value))
        return self


#   Insert a node at a Head - Time Complexity O(N)
    def insert_head(self,var):
        newnode = node(var)
        newnode.next = self.head
        self.head = newnode

#   Insert a node at end of linked_list - Time Complexity O(N)
    def inset_at_end(self,var):
        temp = self.head
        if self.head == None:
            self.head = node(var)
            return
        elif temp.next == None:
             temp.next = node(var)
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = node(var)

#   Insert a node at a position - Time Complexity O(N)
    def inset_at_position(self,position,val):
        if self.head == None:
            print("List is empty")
            return
        newnode = node(val)
        if position == 1:
            newnode.next = self.head
            self.head = newnode
        else:
            count = 1
            temp = self.head
            while count < position-1:
                temp = temp.next
                count = count+1
            newnode.next = temp.next
            temp.next = newnode

#   Insert a node after a certain value in LL- Time Complexity O(N)
    def insert_after_item(self, x, data):
        temp = self.head
        while temp != None:
            if temp.value == x:
                break
            temp = temp.next
        if temp is None:
            print("item not in the list")
        else:
            new_node = node(data)
            new_node.next = temp.next
            temp.next = new_node

#   Insert a node before a certain value in LL- Time Complexity O(N)
    def insert_before_item(self, x, data):
        temp = self.head
        while temp.next != None:
            if temp.next.value == x:
                break
            temp = temp.next
        if temp is None:
            print("item not in the list")
        else:
            new_node = node(data)
            new_node.next = temp.next
            temp.next = new_node

# Function to delete a node at positon
    def delete_node(self,position):
        if position <= 0 or self.head == None:
            return
        if position == 1:
            self.head = head.next
        else:
            temp = self.head
            for _ in range(position-1):
                temp = temp.next
            temp.next = temp.next.next


if __name__ == "__main__":
    ll = linked_list()
    ll.generator(10,1,100)
    print(ll)
    print(len(ll))

    ll.delete_node(3)
    print(ll)
    print(len(ll))
