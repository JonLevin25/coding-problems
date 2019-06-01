#!/usr/bin/env python

def get_pointer(obj):
    pass

def dereference_pointer(pointer):
    pass

class XorLinkedList:
    def __init__(self, head):
        self.head = head
        self.head.both = 0 # "previous" for head is 0, so XOR is just it's pointer

    def get_last_node(self):
        curr = self.head
        prev = None
        nextNode = curr # initialize to curr

        while nextNode != None:
            prev = curr
            curr = nextNode
            nextNode = next(curr, prev)

        return curr


    def next(self, node, previous):
        #edge cases
        if node == None:
            return None
        
        if previous == None:
            return dereference_pointer(node.both)
        
        prevPtr = get_pointer(previous)
        if node.both == prevPtr: #if 'both' is equal to previous, that means 'next' is 0, i.e. None
            return None
        
        nextPtr = node.both ^ prevPtr
        nextNode = dereference_pointer(nextPtr)
        return nextNode

    def previous(self, node, next):
        pass

    def add(self, element):
        lastNode = self.get_last_node()
        lastPtr =get_pointer(lastNode)
        elmPtr = get_pointer(element)

        lastNode.both ^= elmPtr
        element.both = lastPtr
        # TODO: Update count

    def get(self, index):
        curr = self.head
        prev = None
        for i in range(index):
            nextNode = next(curr, prev)
            prev = curr
            curr = nextNode
            if curr == None: 
                break

        return curr

class XorLinkedNode:
    def __init__(self, both):
        self.both = both