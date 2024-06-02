class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insertAfter(prev_node: Node, new_data):
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, index):
        if self.head is None:
            return

        temp: Node | None = self.head

        if index == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = next

    def sort(self):
        current = self.head
        index = Node(None)
        if self.head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next
                current = current.next

    def print(self):
        temp_node = self.head
        while temp_node:
            # print(f"[ {temp_node.data} ({id(temp_node)})|{id(temp_node.next)}]", end=" > " if temp_node.next else "")
            print(f"{temp_node.data}", end=" > " if temp_node.next else "")
            temp_node = temp_node.next
        print()


if __name__ == '__main__':
    linkL = LinkedList()

    linkL.insertAtBeginning(1)
    linkL.insertAtBeginning(2)
    linkL.insertAtBeginning(3)
    linkL.insertAtBeginning(4)
    linkL.insertAtBeginning(5)
    linkL.insertAtBeginning(6)
    linkL.insertAtBeginning(7)
    linkL.insertAtBeginning(8)
    linkL.insertAtBeginning(9)
    # linkL.insertAfter(linkL.head, 2)
    # linkL.print()
    # linkL.print()
    # linkL.delete(3)
    linkL.sort()
    linkL.print()
