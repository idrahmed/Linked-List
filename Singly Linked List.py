class Node:  # Each node has a data value and a next pointer
    def __init__(self, data, next=None):
        self.data = data  # storing data point
        self.next = next  # pointer to the next node. The last element in linked list will have its next pointer set to none


class Linked_list:
    def __init__(self, head=None):
        self.head = head  # used as a placeholder to point to the first element in the linked list

    # Insertion Methods:

    def append(self, data):  # appending new node at end of list
        new_node = Node(data)  # creating new node
        # if list is empty
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head  # node we are currently at
        while current_node.next:  # iterating through nodes while next element is not None
            current_node = current_node.next
        current_node.next = new_node  # setting next node after last element to new node

    def prepend(self, data):  # prepending new node at beginning of list
        new_node = Node(data)
        new_node.next = self.head  # next pointer of new node points to the head
        self.head = new_node  # new node is now the head.

    def insert_after(self, position, data):  # inserting node after a given position
        if position >= self.length() or position < 0:  # Given position must be within the size of list and greater than 0
            print('Position not valid')
            return
        new_node = Node(data)
        current_node = self.head
        if current_node and position == 0:  # Inserting after first element
            self.head = new_node
            new_node.next = current_node

        previous = None  # tracking previous element
        count = 0
        while current_node and position != count:
            previous = current_node
            current_node = current_node.next
            count += 1
        previous.next = new_node  # next pointer of previous node points to new node
        new_node.next = current_node  # next pointer of new node points to next node

    # Delete Methods:

    def delete_index(self, index):  # deleting by index
        if index >= self.length() or index < 0:  # checking if index exists
            print('No element at that position')
            return

        # deleting first element:
        current_node = self.head
        if current_node and index == 0:
            self.head = current_node.next
            return

        # deleting other elements that aren't the first:
        prev_node = None
        count = 0
        while current_node and count != index:  # while current node is not = to index, traverse thru the list
            prev_node = current_node
            current_node = current_node.next
            count += 1

        prev_node.next = current_node.next  # set the previous node's next link to the next node which deletes the current node

    def delete_data(self, data):  # deleting node based on its data value
        # checking if note to be deleted is the first node
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next  # moving head to 2nd node to delete 1st node

            return

        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:  # This means we have traversed through list without finding element
            return

        prev_node.next = current_node.next  # setting the previous node's pointer to the node after the one to be deleted

    def delete_end(self):  # quick method to delete last node
        lastNode = self.head
        prev = None
        while lastNode.next is not None:  # traversing through the list to get the last node
            prev = lastNode
            lastNode = lastNode.next

        prev.next = None  # setting the last node to None

    def display(self):  # displaying the list
        elems = []
        current_node = self.head
        while current_node:  # i.e. while current_node does not equal to None
            elems.append(current_node.data)  # append the data value of the element of elems
            current_node = current_node.next  # go to next node
        print(elems)

    def length(self):  # check length of the list
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def get_element(self, index):  # get element in list via index
        if index >= self.length() or index < 0:  # making sure index entered is not longer than list
            print('Error: Index out of range')
            return None
        current_index = 0  # we will use this to keep track of the index position of values in the list
        current_node = self.head
        while current_node:
            if current_index == index:  # if the current index is equal to inputted index
                return current_node.data  # return the data of the node associated with the current index
            current_node = current_node.next  # else continue traversing the while loop
            current_index += 1  # increment the current index

    def swap_nodes_alt(self, node_1, node_2):  # swap 2 nodes based on data value
        if node_1 == node_2:  # if both inputted nodes are same, then just return
            return
        current_node = self.head
        x, y = None, None  # Assign None to avoid reference error
        while current_node:
            if current_node.data == node_1:
                x = current_node  # node_1 found
            if current_node.data == node_2:
                y = current_node  # node_2 found
            current_node = current_node.next

        if x and y:  # Check if both node's exist
            x.data, y.data = y.data, x.data  # swap
        else:
            return


