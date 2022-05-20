
from secrets import choice


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beg(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            itr = self.head
            while itr.next != None:
                itr = itr.next
            itr.next = new_node  

    def insert_after(self, index, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            itr = self.head
            while itr.data != index:
                itr = itr.next
            new_node.next = itr.next
            itr.next = new_node

    def insert_before(self, index, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        elif self.head.data == index:
            self.insert_at_beg(data)

        else:
            itr = self.head
            while itr.data != index:
                ptr = itr
                itr = itr.next
            new_node.next = itr
            ptr.next = new_node

    def search_list(self, val):
        itr = self.head
        while itr:
            if itr.data == val:
                print("found")
                return itr.data
            itr = itr.next    

    def delete_from_beg(self):
        if self.head == None:
            print("list is already empty")
            return
        if self.head.next == None:
            self.head == None
            return
        itr = self.head
        self.head = self.head.next
        del itr        

    def delete_from_end(self):
        if self.head == None:
            print("list is already empty")
            return
        if self.head.next == None:
            self.head == None
            return
        ptr = None
        itr = self.head
        while itr.next != None:
            ptr = itr
            itr = itr.next
        ptr.next = None
        del itr

    def delete_from_mid(self, val):
        if self.head == None:
            print("list is already empty")
            return
        if self.head.next == None:
            self.head == None
            return
        if self.search_list(val):
            ptr = None
            itr = self.head
            while itr.data != val:
                ptr = itr
                itr = itr.next
            ptr.next = itr.next
            del itr
        else:
            print("element not found")

    def print_list(self):
        if self.head == None:
            print("list is empty")
        else:
            itr = self.head
            while itr:
                print(itr.data, end=" --> ")
                itr = itr.next
            print()

my_list = LinkedList()
choice = 1
while choice:
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert After")
    print("4. Insert Before")
    print("5. Search")
    print("6. Delete from Beginning")
    print("7. Delete from End")
    print("8. Delete from Middle")
    print("9. Print")
    print("10. Quit")
    print("--------------------------------------")

    choice = int(input("enter your choice:"))
    if choice == 1:
        val = input("enter value")
        my_list.insert_at_beg(val)
        print("--------------------------------------")
    elif choice == 2:
        val = input("enter value")
        my_list.insert_at_end(val)
        print("--------------------------------------")
    elif choice == 3:
        val = input("enter value")
        index = input("enter value of element after which you wish to insert the element")
        my_list.insert_after(index, val)
        print("--------------------------------------")
    elif choice == 4:
        val = input("enter value")
        index = input("enter value of element before which you wish to insert the element")
        my_list.insert_before(index, val)
        print("--------------------------------------")
    elif choice == 5:
        val = input("enter value")
        my_list.search_list(val)
        print("--------------------------------------")
    elif choice == 6:
        my_list.delete_from_beg()
        print("--------------------------------------")
    elif choice == 7:
        my_list.delete_from_end()
        print("--------------------------------------")
    elif choice == 8:
        val = input("enter value")
        my_list.delete_from_mid(val)
        print("--------------------------------------")
    elif choice == 9:
        my_list.print_list()
        print("--------------------------------------")
    elif choice == 10:
        break 
    else:
        print("enter a valid choice")
        print("--------------------------------------")
        







                