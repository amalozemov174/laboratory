import linkedList2_1
from linkedList2_1 import Node

#2.10.* Добавьте метод, который "переворачивает" порядок элементов в связном списке, меняя его на противоположный.
def reverse_linked_list(linkedList):
    if linkedList.len() <= 1:
        return linkedList
    node = linkedList.head
    while node is not None:
        if node is not None:
            tmp = node
            node_next = tmp.next
            node_prev = tmp.prev
            if node.next is not None and node.prev is not None:
                node.next = node_prev
                node.prev = node_next
                node = node_next
            else:
                if node_next is None:
                    node.next = tmp.prev
                    node.prev = None
                    node = node_next
                    linkedList.head = tmp
                if node_prev is None:
                    node.prev = tmp.next
                    node.next = None
                    node = node_next
                    linkedList.tail = tmp

#2.11.* Добавьте булев метод, который сообщает, имеются ли циклы (замкнутые на себя по кругу) внутри списка.
def has_cycle(self):
    visited = {}
    node = self.head
    while node is not None:
        if node in visited:
            return True
        visited[node] = True
        node = node.next
    visited = {}
    node = self.tail
    while node is not None:
        if node in visited:
            return True
        visited[node] = True
        node = node.prev

#2.12.* Добавьте метод, сортирующий список.
def sort(linkedList):
    if linkedList.len() > 1:    
        node = linkedList.head
        while node is not None:            
            node1 = node.next
            while node1 is not None:
                if node.value >  node1.value:
                    tmp = node1.value
                    node1.value = node.value     
                    node.value = tmp
                node1 = node1.next
            node = node.next  

#2.13.* Добавьте метод, объединяющий два списка в третий. Эти списки предварительно надо отсортировать, и выдать результирующий список, в котором все элементы также будут упорядочены (для результирующего списка использовать метод сортировки не разрешается).
def merge(linkedList1, linkedList2):
    res = LinkedList2()
    sort(linkedList1)
    sort(linkedList2)
    node1 = linkedList1.head
    node2 = linkedList2.head
    while node1 is not None and node2 is not None:
        if node1.value > node2.value:
            res.add_in_tail(Node(node2.value))
            node2 = node2.next
        else:
            res.add_in_tail(Node(node1.value))
            node1 = node1.next
    if node1 is None:
        while node2 is not None:
            res.add_in_tail(Node(node2.value))    
            node2 = node2.next    
    else:
        while node1 is not None:
            res.add_in_tail(Node(node1.value))    
            node1 = node1.next
    return res 

#2.14.*
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class DummyNode(Node):
    def __init__(self):
        super().__init__(None)

class LinkedList2:  
    def __init__(self):        
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
