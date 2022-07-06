class Node:

    """
    An object for storing a single node of a linked list.
    Models two attributes: data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Returns the number of Nodes in the list
    Takes 0(n)-linear time
    Singly Linked list
    """

    #head = None

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds new node containing data at the head of the list
        Takes O(1)-constant time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node 


    def search(self, key):
        """
        Search for the first Node containing data that matches the key
        Returns Node or None isf not found
        Takes O(n)-linear Time 
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        
        return None



    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n)-linear time
        """

        nodes = []
        current = self.head

        while current != None:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
        
        return '->'.join(nodes)