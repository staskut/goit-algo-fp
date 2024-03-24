class ListNode:
    """
    Represents a node in a linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    """
    Implements a linked list data structure.
    """
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Inserts a new node containing 'data' at the beginning of the list.
        """
        new_node = ListNode(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a new node containing 'data' at the end of the list.
        """
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def insert_after(self, previous_node: ListNode, data):
        """
        Inserts a new node containing 'data' after the given 'previous_node'.
        Raises an error if 'previous_node' is not found.
        """
        if previous_node is None:
            print("Previous node not found!")
            return
        new_node = ListNode(data)
        new_node.next_node = previous_node.next_node
        previous_node.next_node = new_node

    def delete_node(self, key: int):
        """
        Deletes the first node containing the value 'key'.
        """
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next_node
            current_node = None
            return
        previous_node = None
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next_node
        if current_node is None:
            return
        previous_node.next_node = current_node.next_node
        current_node = None

    def search(self, data: int) -> ListNode | None:
        """
        Searches for a node containing the value 'data' and returns the node if found, otherwise returns None.
        """
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next_node
        return None

    def print_list(self):
        """
        Prints the data of each node in the list.
        """
        current_node = self.head
        str_repr = []
        while current_node:
            str_repr.append(str(current_node.data))
            current_node = current_node.next_node
        print(" -> ".join(str_repr))

    def merge_sort_linked_list(self, head):
        """
        Sorts a linked list using the merge sort algorithm.
        Args:
            head (ListNode): The head of the linked list to be sorted.
        Returns:
            ListNode: The head of the sorted linked list.
        """
        if head is None or head.next_node is None:
            return head

        mid = self.get_middle(head)
        mid_next = mid.next_node
        mid.next_node = None

        left = self.merge_sort_linked_list(head)
        right = self.merge_sort_linked_list(mid_next)

        return self.merge(left, right)

    def get_middle(self, head):
        """
        A function to find the middle element of a linked list given the head node.
        Parameters:
            self: the instance of the class
            head: the head node of the linked list
        Returns:
            The middle element of the linked list
        """
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next_node and fast.next_node.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node

        return slow

    def merge(self, left, right):
        """
        Merge two linked lists recursively based on the data in each node.
        Parameters:
        left (ListNode): The head of the first linked list.
        right (ListNode): The head of the second linked list.
        Returns:
        ListNode: The head of the merged linked list.
        """
        if left is None:
            return right
        if right is None:
            return left

        if left.data < right.data:
            result = left
            result.next_node = self.merge(left.next_node, right)
        else:
            result = right
            result.next_node = self.merge(left, right.next_node)

        return result

    def reverse_list(self):
        """
        Reverses the order of nodes in the linked list.
        """
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def merge_sorted_lists(self, head1, head2):
        """
        Merges two sorted linked lists and returns the head of the merged list.
        """
        dummy_node = ListNode(0)
        tail = dummy_node

        while True:
            if head1 is None:
                tail.next_node = head2
                break
            if head2 is None:
                tail.next_node = head1
                break

            if head1.data <= head2.data:
                tail.next_node = head1
                head1 = head1.next_node
            else:
                tail.next_node = head2
                head2 = head2.next_node

            tail = tail.next_node

        return dummy_node.next_node


# Створення першого списку: 1 -> 3 -> 5
llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)
llist1.print_list()

# Створення другого списку: 2 -> 4 -> 6
llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)
llist2.print_list()

# Об'єднання відсортованих списків
merged_list = LinkedList()
merged_list.head = merged_list.merge_sorted_lists(llist1.head, llist2.head)

# Виведення об'єднаного списку
merged_list.print_list()  # Виведення списку: 1 -> 2 -> 3 -> 4 -> 5 -> 6
# reverse
merged_list.reverse_list()
merged_list.print_list()  # 6 -> 5 -> 4 -> 3 -> 2 -> 1
