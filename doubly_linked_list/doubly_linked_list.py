from doubly_linked_list.node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head : Node = None
        self.tail : Node = None

    def containsNodeWithValue(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        return None

    def remove(self, node: Node):
        if(self.head == node):
            self.head = node.next
        elif(self.tail == node):
            self.tail = node.prev

        self.removeNodeBindings(node)

    def removeNodeBindings(self, node: Node):
        tempPrev = node.prev
        tempNext = node.next
        node.prev = None
        node.next = None
        if tempPrev is not None:
            tempPrev.next = tempNext
        if tempNext is not None:
            tempNext.prev = tempPrev

    def removeNodesWithValue(self, value):
        node = self.head
        deletedCount = 0
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
                deletedCount += 1

        return deletedCount

    def insertBefore(self, node: Node, nodeToInsert: Node):
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is not None:
            node.prev.next = nodeToInsert
        else: # node is head
            self.head = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node: Node, nodeToInsert: Node):
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is not None:
            node.next.prev = nodeToInsert
        else:
            self.tail = nodeToInsert
        node.next = nodeToInsert

    def setHead(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node: Node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertAtPosition(self, position, nodeToInsert):
        if position == 0:
            self.setHead(nodeToInsert)
            return
        currentNode = self.head
        currentPosition = 0
        while currentNode is not None and currentPosition != position:
            currentNode = currentNode.next
            currentPosition += 1
        if currentNode is not None: # we are not at the tail
            self.insertBefore(currentNode, nodeToInsert)
        else:
            self.setTail(nodeToInsert)