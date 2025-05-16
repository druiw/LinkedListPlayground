class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            return

        curr = self.head

        while curr.next:
            curr = curr.next
        curr.next = newNode

    def printList(self):
        curr = self.head

        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
    
    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def deleteNode(self, data):
        curr = self.head
        prev = None

        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return
            prev = curr
            curr = curr.next
        
        

if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        user_input = input("Enter a value to add to the linked list (or type 'exit' to stop): ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "front":
            user_input = input("Enter a value to insert at beginning: ")
            linked_list.insertAtBeginning(user_input)
        elif user_input.lower() == "delete":
            user_input  = input("Enter a value to delete from the linked list: ")
            linked_list.deleteNode(user_input)
        else:
            linked_list.append(user_input)
        print("Current Linked List:")
        linked_list.printList()