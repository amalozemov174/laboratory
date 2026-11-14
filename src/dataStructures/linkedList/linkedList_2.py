def sumItems(linkedList1, linkedList2):
    res = []
    node1 = linkedList1.head
    node2 = linkedList2.head
    if linkedList1.len() != linkedList2.len():
        return res
    while node1 is not None and node2 is not None:
        res.append(node1.value + node2.value)
        node1 = node1.next    
        node2 = node2.next    
    return res 