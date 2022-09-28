from dynamicArray import DynamicArray
from linkedList import *
from doublyLinkedList import *
from myStack import *
from myQueue import *
from myHashTable import *

print("\n\n")
print("--------------------Dynamic Array (dynamicArray.py)--------------------")
print("\n\n")
#create a new dynamic array
arr = DynamicArray()
#append some numbers
arr.append(1)
arr.append(2)
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
#print dynamic array
arr.print_arr()
#delete method
arr.delete()
arr.print_arr()
#insert Method
arr.insertAt(5,1)
arr.print_arr()
#removeAt
arr.removeAt(1)
arr.print_arr()
# List to dynamic array
arr2 = DynamicArray()
listA = [1,2,3,4,5,10]
arr2.insertList(listA)
arr2.print_arr()



print("\n\n")
print("--------------------Linked List (linkedList.py)--------------------")
print("\n\n")
# Create a new linked list
linkedList1 = SLinkedList()
# Append some values
linkedList1.append(5)
linkedList1.append(6)
linkedList1.append(8)
# print linked list
linkedList1.listPrint()
# prepend to the linked list
linkedList1.prepend(4)
# print linked list again
linkedList1.listPrint()
# Insert between a linked list
linkedList1.insertBetween(4,7)
# print linked list again
linkedList1.listPrint()
# delete first node
linkedList1.removeFirstNode()
# print linked list again
linkedList1.listPrint()
# Remove a node with a key
linkedList1.removeKeyElement(6)
# print linked list again
linkedList1.listPrint()
#Try to remove a node that does not exist
linkedList1.removeKeyElement(25)


print("\n\n")
print("--------------------Doubly Linked List (doublyLinkedList.py)--------------------")
print("\n\n")
# Single Linked List VS Doubly Linked List
# Time complexity for insertion and deletion for single linked list is O(n)
# Time complexity for insertion and deletion for doubly linked list is O(1)
# You can traverse both way with doubly linked list
# Single linked list: consumes less memory
# Create a new doubly linked list
linkedList2 = dLinkedList()
# append some values
linkedList2.append(10)
linkedList2.append(11)
linkedList2.append(12)
# print doubly linked list
linkedList2.printNode()
# preppend some values
linkedList2.prepend(9)
linkedList2.printNode()
# removeFirstNode
linkedList2.removeFirstNode()
linkedList2.printNode()
# remove last Node
linkedList2.removeLastElement()
linkedList2.printNode()


print("\n\n")
print("--------------------Stack(stack.py)--------------------")
print("\n\n")
# create a stack
newStack= myStack(1)
# print stack
newStack.printStack()
# push elements to the stack
newStack.push(2)
newStack.push(3)
newStack.push(4)
# print stack
newStack.printStack()
#pop stack
newStack.pop()
# pop stack again
newStack.pop()
# print stack
newStack.printStack()
# push more values
newStack.push(5)
# push more values
newStack.push(6)
# push more valuesgit 
newStack.push(7)
# print stack
newStack.printStack()
# peack
newStack.peak()
# Size of the stack
newStack.size()


print("\n\n")
print("--------------------Queue(stack.py)--------------------")
print("\n\n")

# Initialize queue with its size
myQueue1 = MyQueue(5)
# enqueue some numbers to the queue
myQueue1.myEnqueue(1)
myQueue1.myEnqueue(2)
myQueue1.myEnqueue(3)
myQueue1.myEnqueue(4)
myQueue1.myEnqueue(5)
myQueue1.printMyQueue()

# queue overflow should print error
myQueue1.myEnqueue(6)

# dequeue 
myQueue1.myDequeue()
myQueue1.myDequeue()
myQueue1.myDequeue()
# print queue again
myQueue1.printMyQueue()


# Enqueue some numbers again
myQueue1.myEnqueue(6)
myQueue1.printMyQueue()

# dequeu again
myQueue1.myDequeue()
# print queue again
myQueue1.printMyQueue()




