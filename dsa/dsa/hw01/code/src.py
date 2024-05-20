class Node:  #class for the nodes in the linked list
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:  #class for the Linked List data structure used to store and sort the data before it is placed in the
    # output file
    def __init__(self):
        self.head = None

    def append(self, data):  #appends data to the linked list. Uses the contain method to check if data is already in
        # the linked list and excludes multiple occurrences of the same integer
        if not self.contains(data):  #Ensures that integers in the linked list are unique.
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current_node = self.head
                while current_node.next is not None:
                    current_node = current_node.next
                current_node.next = new_node

    def contains(self, data):  #Checks to see if Linked-list already contains an integer. Returns True if it does, else
        # False
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def display(self):  #Displays elements in the Linked List
        elements = []
        current_node = self.head
        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)

    def sort(self, data):  #Sorts integers in ascending order in the linked list. data = integers
        if not self.contains(data):  # Ensures uniqueness
            new_node = Node(data)
            if self.head is None or self.head.data >= data:  # Insert at the head or before the first element
                new_node.next = self.head
                self.head = new_node
            else:
                current_node = self.head
                while current_node.next is not None and current_node.next.data < data:
                    current_node = current_node.next
                new_node.next = current_node.next
                current_node.next = new_node


class UniqueInt:
    def __init__(self):
        self.list = LinkedList()

    def trim(self, line):  # Removes white-spaces on either side of the integer in the input file
        trimmed_line = ""
        word_count = 0
        for character in line:
            if character not in {' ', '\t', '\n', '\r', '\v', '\f'}:
                trimmed_line += character
            elif trimmed_line:
                word_count += 1
                if word_count >= 2:
                    return None
        return trimmed_line if trimmed_line else None
        #Returns the integer sting if it exits for every line

    def is_integer(self, line):  #Checks if a line is a valid integer excluding other data types
        trimmed_line = self.trim(line)
        if trimmed_line is None:
            return False
        try:
            integer_value = int(trimmed_line)  # Converts trimmed string to an integer data type
            if -1023 <= integer_value <= 1023:  #Excludes integer if it is out of the desired range
                return True
            else:
                return False
        except ValueError:
            return False

    def read_next_item_from_file(self, input_file):  #reads through the input file line by line if it is a valid integer
        for line in input_file:
            if self.is_integer(line):
                return int(self.trim(line))
        return None

    def process_file(self, input_file_path, output_file_path):   #The main method. This method is executed after
        # importing the class to give the desired output
        with open(input_file_path) as input_file: #Opens an input file with the given file path
            next_integer = self.read_next_item_from_file(input_file) #Reads through every line in the file
            while next_integer is not None:
                self.list.sort(next_integer)  #Sorts integers in ascending order
                next_integer = self.read_next_item_from_file(input_file)

        with open(output_file_path, 'w') as output_file:  #Opens an output file and wries the desird output in the file
            current_node = self.list.head
            while current_node is not None:
                output_file.write(str(current_node.data) + '\n')
                current_node = current_node.next
