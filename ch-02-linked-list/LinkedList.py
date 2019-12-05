import random
class Node():

    def __init__(self,vlaue):
        self.value  = vlaue
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

# Make the LinkedList Iterable
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

#   Insert a Node at a Head - Time Complexity O(N)
    def insert_head(self,var):
        newNode = Node(var)
        newNode.next = self.head
        self.head = newNode

#   Insert a Node at end of LinkedList - Time Complexity O(N)
    def inset_at_end(self,var):
        temp = self.head
        if self.head == None:
            self.head = Node(var)
            return
        elif temp.next == None:
             temp.next = Node(var)
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = Node(var)

#   Insert a Node at a position - Time Complexity O(N)
    def inset_at_position(self,position,val):
        if self.head == None:
            print("List is empty")
            return
        newNode = Node(val)
        if position == 1:
            newNode.next = self.head
            self.head = newNode
        else:
            count = 1
            temp = self.head
            while count < position-1:
                temp = temp.next
                count = count+1
            newNode.next = temp.next
            temp.next = newNode

#   Insert a Node after a certain value in LL- Time Complexity O(N)
    def insert_after_item(self, x, data):
        temp = self.head
        while temp != None:
            if temp.value == x:
                break
            temp = temp.next
        if temp is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

#   Insert a Node before a certain value in LL- Time Complexity O(N)
    def insert_before_item(self, x, data):
        temp = self.head
        while temp.next != None:
            if temp.next.value == x:
                break
            temp = temp.next
        if temp is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

if __name__ == "__main__":
    ll = LinkedList()
    ll.generator(10,1,100)
    print(ll)
    print(len(ll))
