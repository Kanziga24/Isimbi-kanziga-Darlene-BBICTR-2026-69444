"""
Task 4: Linked List
Contributor: Member C

Singly Linked List with insert-at-head, insert-at-tail,
delete-by-value, and traverse/print.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        # Time Complexity: O(1) - new node just points to old head
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_at_tail(self, value):
        # Time Complexity: O(n) - must walk to the last node
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def delete_by_value(self, value):
        # Time Complexity: O(n) - may need to scan the whole list
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            return True

        prev = self.head
        current = self.head.next
        while current:
            if current.value == value:
                prev.next = current.next
                return True
            prev = current
            current = current.next

        return False  # value not found

    def traverse(self):
        # Time Complexity: O(n) - visits every node once
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        print(" -> ".join(values) if values else "(empty list)")


if __name__ == "__main__":
    ll = LinkedList()

    print("-- Insert at tail: 10, 20, 30 --")
    ll.insert_at_tail(10)
    ll.insert_at_tail(20)
    ll.insert_at_tail(30)
    ll.traverse()

    print("\n-- Insert at head: 5 --")
    ll.insert_at_head(5)
    ll.traverse()

    print("\n-- Delete value 20 --")
    ll.delete_by_value(20)
    ll.traverse()

    print("\n-- Delete value 5 (head) --")
    ll.delete_by_value(5)
    ll.traverse()

    print("\n-- Attempt to delete non-existent value 99 --")
    found = ll.delete_by_value(99)
    print("Found and deleted:", found)
    ll.traverse()
