class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def Print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def Append(self, value):
        # Edge case - When LL has no Elements
        node = Node(value)
        if self.head is not None:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.head = node
        self.length += 1
        return True
    
    def Pop(self):
        # Edge case - When LL has no Elements
        # Edge case - When LL has only one Elements
        if self.length == 0:
            return None

        pointer = self.head
        pop = self.head

        while pop.next is not None:
            pointer = pop
            pop = pop.next

        self.tail = pointer
        self.tail.next = None
        self.length -= 1
        
        if self.length == 0:
            self.tail = None
            self.head = None

        return pop

    def Prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def Drop(self):
        if self.length == 0:
            return None
        
        droppedNode = self.head
        self.head = self.head.next
        droppedNode.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return droppedNode

    def Get(self, index):
        if index < 0 or index >= self.length:
            return None

        pointer = self.head
        for _ in range(index):
            pointer = pointer.next

        return pointer

    def SetValue(self, index, value):
        pointer = self.Get(index)

        if pointer:
            pointer.value = value
            return True

        return False

    def Insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.Prepend(value)
        if index == self.length:
            return self.Append(value)

        node = Node(value)
        pointer = self.Get(index-1)

        node.next = pointer.next
        pointer.next = node
        self.length += 1

        return True

    def Remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.Drop()
        if index == self.length:
            return self.Pop()

        prevPointer = self.Get(index-1)
        pointer = prevPointer.next

        prevPointer.next = pointer.next
        pointer.next = None
        self.length -= 1
        return pointer

    def Reverse(self):
        pointer = self.head
        self.head = self.tail
        self.tail = pointer

        after = self.head.next
        before = None

        for _ in range(self.length):
            after = pointer.next
            pointer.next = before
            before = pointer
            pointer = after
        
# print(type(linkedList.head)) Output: <class '__main__.Node'>
# print(linkedList.head) Output: <__main__.Node object at 0x7f8fe7d97d60>

linkedList = LinkedList(1)
linkedList.Append(2)
linkedList.Append(3)
linkedList.Print()
poppedNode = linkedList.Pop()
print(poppedNode.value)
linkedList.Prepend(0)
linkedList.Drop()
print(linkedList.Get(1).value)
linkedList.SetValue(1, 0)
linkedList.Insert(2, -1)
linkedList.Print()
linkedList.Remove(3)
linkedList.Print()
linkedList.Reverse()
linkedList.Print()
