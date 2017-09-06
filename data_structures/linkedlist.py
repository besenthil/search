
class Node(object):
    def __init__(self,data,next_node=None):
        self.data=data
        self.next_node = next_node

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
        self.tail=None

    def append(self,data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while (current_node.next_node is not None):
                current_node = current_node.next_node
            current_node.next_node = node
            self.tail=node
            self.set_size(data,'APPEND')

    def set_size(self,data,operation):
        if operation == 'APPEND' and data is not None :
            self.size += data.__sizeof__()
        elif operation == 'DELETE' and data is not None:
            self.size -= data.__sizeof__()
            self.size = 0 if self.size < 0 else self.size

    def list(self):
        current_node = self.head
        while (current_node is not None):
            print (current_node.data,end="")
            current_node = current_node.next_node

    def delete(self,data):
        if self.head is None or data == '' or data is None:
            return False

        current_node = self.head
        previous_node = self.head
        self.set_size(data,'DELETE')

        if current_node.data == data:
            self.head = current_node.next_node
            return current_node

        while (current_node is not None and current_node.data != data):
            previous_node = current_node
            current_node = current_node.next_node

        if current_node is None:
            return False
        if current_node.data == data and current_node.next_node is not None:
            previous_node.next_node = current_node.next_node
            return current_node.data


    def deleteAll(self):
        if self.head is None:
            return False

        while (self.head is not None):
            self.delete(self.head.data)

    def pop(self):
        if self.head is None:
            return False

        pointer = self.head

        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            return data

        while pointer.next_node is not self.tail:
            print (pointer.next_node,self.tail)
            pointer = pointer.next_node

        data= pointer.next_node.data
        pointer.next_node = None
        self.tail = pointer
        return data



if __name__ == "__main__":
    linked_list = LinkedList()
    for x in range(0,10):
        linked_list.append(100)
    #linked_list.list()
    print (linked_list.size)
    for x in range(0,11):
        print(linked_list.delete(x))
        print("Deleted")    #linked_list.delete(1900)
    print("Size")
    print (linked_list.size)
    for x in range(0,10):
        linked_list.append(x)
    print (linked_list.size)
    #linked_list.deleteAll()
    #print("deletedall")
    print (linked_list.size)
    for x in range(0,1000):
        print(linked_list.pop())