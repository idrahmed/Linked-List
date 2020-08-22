class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            new_node.prev = current_node
            current_node.next = new_node
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data and current == self.head:
                # Case 1:
                if not current.next:
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    self.head = nxt
                    return

            elif current.data == data:
                # Case 3:
                if current.next:
                    nxt = current.next
                    pre = current.prev
                    pre.next = nxt
                    nxt.prev = pre
                    current.next = None
                    current.prev = None
                    return

                # Case 4:
                else:
                    pre = current.prev
                    pre.next = None
                    current.prev = None
                    return

            current = current.next


    def delete_index(self, index):
        current = self.head

        if index >= self.length() or index < 0:
            print('No node at that position')
            return

        if current is None:
            print('Empty List')
            return

        if current.next is None and index == 0:
            self.head = None
            return
        # if want to delete first node:
        if current and index == 0:
            current.next.prev = None
            self.head = current.next
            return

        # if want to delete last node:

        count = 0
        prev = None
        while current:
            if index == count and current.next is None:
                prev.next = None

            if index == count and current.next is not None:
                prev.next = current.next
                current.next.prev = prev

                return

            prev = current
            current = current.next
            count += 1

    def add_after(self, value, data):
        current = self.head


        while current:
            if current.next is None and current.data == value:
                self.append(data)
                return
            elif current.data == value:
                new_node = Node(data)
                nxt = current.next
                current.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
                new_node.prev = current


            current = current.next


    def add_before(self, value, data):
        current = self.head
        while current:
            if current.prev is None and current.data == value:
                self.prepend(data)
                return
            elif current.data == value:
                new_node = Node(data)
                pre = current.prev
                pre.next = new_node
                new_node.next = current
                current.prev = new_node
                new_node.prev = pre

            current = current.next


    def print_list(self):
        elems = []
        current_node = self.head
        while current_node:
            elems.append(current_node.data)
            current_node = current_node.next
        print(elems)


