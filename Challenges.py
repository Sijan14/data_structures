# Project 506

# Here are some problem-solving challenges that can be tackled using various data structures in Python.
# Use these exercises to explore the practical application of various data structures in solving a range of problem-solving challenges. 
# The goal is to implement and utilize different data structures within Python to tackle diverse problem scenarios effectively.
# This project aims to foster a deeper appreciation and proficiency in leveraging Python's data structures for effective problem-solving.


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# 1- Use a stack to check if a given string is a palindrome.
# Problem Statement: Palindrome Checker
# Write a Python function is_palindrome() that takes a string as input and uses a stack to determine if the input string is a palindrome or not.
# A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
# Your function should return True if the input string is a palindrome and False otherwise.

#Example:
"""
Input: "racecar"
Output: True

Input: "hello"
Output: False
"""

# Guidelines:

# - Implement a stack data structure using a list.
class Stack:
    def __init__(self):
        self.stack_list = []

    def pop(self):
        return self.stack_list.pop()
    
    def push(self, item):
        self.stack_list.append(item)

    def length(self):
        return len(self.stack_list)

# - Ignore spaces and punctuation when checking for a palindrome.
# - Use Python's built-in string manipulation functions (such as lower(), isalpha(), etc.) as needed for preprocessing the input string.
def is_palindrome(word):
    # word pre-processing
    cleaned_word = ''.join(c for c in word if c.isalpha())

    # add the letters to the stack
    letter_stack = Stack()
    for letter in cleaned_word:
        letter_stack.push(letter)
    
    # check if palidrome
    for letter in cleaned_word:
        reverse = letter_stack.pop()
        if letter != reverse:
            return False
        
    return True

# input from the user
"""
word = input("Input: ").strip().lower()
print(f'Output: {is_palindrome(word)}')
"""

# Test Cases: # Test your function with the following test cases:
# Input: "level"
# Expected Output: True
# Input: "A man, a plan, a canal, Panama"
# Expected Output: True
# Input: "hello"
# Expected Output: False
# Input: "Was it a car or a cat I saw?"
# Expected Output: True

# Feel free to explore different approaches and use the stack concept to validate whether a given string is a palindrome or not.

## Defining a Python Stack using a list


# ---------------------------------------------------------------------------------------------------------------------------
# 2- Create a queue data structure using two stacks and implement its enqueue and dequeue operations.
# Problem Statement: Implementing a Queue using Stacks
# Create a Python class QueueWithStacks that implements a queue data structure using two stacks. Implement the enqueue() and dequeue() operations for this queue.
# The enqueue() operation should add an element to the queue, and the dequeue() operation should remove and return the first element added to the queue.
# Use two stacks (stack_1 and stack_2) to simulate the queue behavior. You can use Python lists to represent the stacks.
class QueueWithStacks:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, item):
        self.stack_1.push(item)

    def dequeue(self):
        while self.stack_1.length():
            item = self.stack_1.pop()
            self.stack_2.push(item)
        
        if self.stack_2.length():
            return self.stack_2.pop()
            
        

#Example:

queue = QueueWithStacks()
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)

print(queue.dequeue())  # Output: 5
print(queue.dequeue())  # Output: 10

#Guidelines:

#Implement the queue using two stacks (lists).
#For the enqueue() operation, add elements to stack_1.
#For the dequeue() operation, if stack_2 is empty, transfer elements from stack_1 to stack_2 to simulate FIFO behavior.
#Ensure that the dequeue() operation returns elements in the order they were added (FIFO).
#Test Cases: Test your implementation with the following test cases:

"""
Enqueue 3 elements: 5, 10, 15
 - Perform dequeue(). Expected Output: 5
 - Perform dequeue(). Expected Output: 10
Enqueue elements: 20, 25, 30, 35
 - Perform dequeue() twice. Expected Output: 20, 25
Enqueue elements: 'a', 'b', 'c', 'd', 'e'
 - Perform dequeue() thrice. Expected Output: 'a', 'b', 'c'

"""
# Make sure that the queue operations (enqueue() and dequeue()) follow the FIFO (First-In-First-Out) order, simulating the behavior of a queue using two stacks.





# ---------------------------------------------------------------------------------------------------------------------------
# 3- Use a dictionary to count the frequency of words in a given text.
# Problem Statement: Word Frequency Counter
# Create a Python function word_frequency_counter() that takes a text string as input and uses a dictionary to count the frequency of each word in the text.
# Your function should return a dictionary where the keys are unique words in the text, and the values are the frequencies of those words.

#Example
"""
text = "This is a sample text. This text will be used to count word frequency."
result = word_frequency_counter(text)
print(result)

"""

#Expected Output
"""
{
    'This': 2,
    'is': 1,
    'a': 1,
    'sample': 1,
    'text': 2,
    'will': 1,
    'be': 1,
    'used': 1,
    'to': 1,
    'count': 1,
    'word': 1,
    'frequency': 1
}
"""
# Guidelines:
# Use a dictionary to store word frequencies.
# Split the text into words and iterate through each word.
# Update the dictionary by incrementing the count for each word encountered.


# Test Cases: Test your function with the following test cases:
# Input: "Python is a powerful programming language. Python is used in various domains."
"""
{
    'Python': 2,
    'is': 2,
    'a': 1,
    'powerful': 1,
    'programming': 1,
    'language': 1,
    'used': 1,
    'in': 1,
    'various': 1,
    'domains': 1
}
"""






# ---------------------------------------------------------------------------------------------------------------------------
# 4- Implement a function to check if a given string of parentheses is balanced using a stack.
# Problem Statement: Balanced Parentheses Checker
# Create a Python function is_balanced_parentheses() that takes a string containing only parentheses (( and )) as input and uses a stack to check if the parentheses are balanced.
# A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis and they occur in the correct order.
# Your function should return True if the parentheses are balanced and False otherwise.

# Example:
"""
string_1 = "()((()))"
string_2 = "(()())("
print(is_balanced_parentheses(string_1))  # Output: True
print(is_balanced_parentheses(string_2))  # Output: False
"""

# Guidelines:
# Use a stack to keep track of opening parentheses.
# Iterate through the string, pushing opening parentheses onto the stack and popping the stack when encountering a closing parenthesis.
# Check for balance by ensuring that for every closing parenthesis encountered, there exists a corresponding opening parenthesis in the stack.

# Test Cases: Test your function with the following test cases:

"""
Input: "((()))()"
Expected Output: True
Input: "((())"
Expected Output: False
Input: "()()()()"
Expected Output: True
"""

# Ensure that the function accurately determines whether a given string of parentheses is balanced or not using a stack-based approach.





# ---------------------------------------------------------------------------------------------------------------------------
# 5-Implement operations such as insertion, deletion, and searching in a binary search tree.

# Problem Statement: Binary Search Tree (BST) Operations
# Create a Python class BinarySearchTree that represents a binary search tree. Implement operations such as insertion, deletion, and searching in the binary search tree.
# The class should have the following methods:

# insert(value): Inserts a new node with the given value into the binary search tree.
# delete(value): Deletes a node with the given value from the binary search tree, if present.
# search(value): Searches for a node with the given value in the binary search tree. Returns True if the value is found, False otherwise.
# Ensure that the binary search tree maintains its property where for each node:

# The left subtree of a node contains only nodes with values less than the node's value.
# The right subtree of a node contains only nodes with values greater than the node's value.

# Example
"""
# Create an instance of the BinarySearchTree class
bst = BinarySearchTree()

# Insert values into the binary search tree
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

# Search for values in the binary search tree
print(bst.search(7))  # Output: True
print(bst.search(11))  # Output: False

# Delete a value from the binary search tree
bst.delete(15)
print(bst.search(15))  # Output: False

"""

# Guidelines:

# Implement the BinarySearchTree class with appropriate methods to perform insertion, deletion, and searching operations.
# Ensure that after deletion, the BST property is maintained.
# Consider edge cases such as deleting nodes with no children, one child, or two children.
# For deletion, you may choose to implement any method (like replacing with the minimum value from the right subtree or the maximum value from the left subtree) for maintaining the BST property.

# Test Cases:
# Test your implementation with various scenarios including insertion, deletion, and searching for values in the binary search tree. Ensure that the operations are correctly performed while maintaining the BST property.

# ---------------------------------------------------------------------------------------------------------------------------
# 6-	Graph Traversal: Implement depth-first search (DFS) and breadth-first search (BFS) algorithms for traversing a graph.



# ---------------------------------------------------------------------------------------------------------------------------
# 7- Use a set to find duplicates in an array or list efficiently.
# Problem Statement: Finding Duplicates
# Create a Python function find_duplicates() that takes a list or array as input and efficiently finds and returns a set containing all the duplicate elements present in the input list.
# Your function should utilize a set to efficiently identify and collect duplicate elements from the given list.


# Example 
"""
arr_1 = [1, 2, 3, 4, 4, 2, 5, 6, 3]
arr_2 = ['a', 'b', 'c', 'b', 'd', 'e', 'a']

result_1 = find_duplicates(arr_1)
result_2 = find_duplicates(arr_2)

print(result_1)  # Output: {2, 3, 4}
print(result_2)  # Output: {'b', 'a'}
"""

# Guidelines:

# Iterate through the input list.
# Use a set to store elements seen so far.
# When iterating, if an element is already in the set, add it to the duplicates set.
# Test Cases: Test your function with the following test cases:
"""
Input: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
Expected Output: {1, 2, 3, 4, 5}
Input: ['x', 'y', 'z', 'x', 'y', 'x', 'z']
Expected Output: {'x', 'y', 'z'}
Input: [1, 2, 3, 4, 5]
Expected Output: set()
"""
#Ensure that the find_duplicates() function efficiently identifies and returns a set containing all the duplicate elements present in the given list without modifying the original list.


# ---------------------------------------------------------------------------------------------------------------------------
# 8- Implement a function to reverse a linked list using pointers.
# Problem Statement: Reverse a Linked List

# Create a Python function reverse_linked_list() that takes the head of a linked list as input and reverses the linked list by manipulating pointers.
# The function should return the new head of the reversed linked list.
# Each node in the linked list is represented by a class Node having value and next attributes.

# Example
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Reverse the linked list
reversed_head = reverse_linked_list(head)

# Print the reversed linked list: 5 -> 4 -> 3 -> 2 -> 1
while reversed_head:
    print(reversed_head.value, end=" -> ")
    reversed_head = reversed_head.next
print("None")
"""

# Guidelines:

# Use three pointers to reverse the linked list: prev, current, and next_node.
# Traverse through the linked list while manipulating pointers to reverse the direction of the links.

# Test Cases: Test your function with various linked list scenarios:

# Input: 1 -> 2 -> 3 -> 4 -> 5
# Expected Output: 5 -> 4 -> 3 -> 2 -> 1
# Input: 2 -> 4 -> 6 -> 8 -> 10
# Expected Output: 10 -> 8 -> 6 -> 4 -> 2

# Ensure that the reverse_linked_list() function correctly reverses the given linked list by manipulating pointers, resulting in a reversed linked list with its head node returned.

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# These challenges cover a range of data structures—stacks, queues, dictionaries, sets, graphs, heaps, linked lists, and trees—allowing for practical application and understanding of different data structure functionalities in problem-solving scenarios.
