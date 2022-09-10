from dynamicArray import DynamicArray

print("--------------------Dynamic Array--------------------")
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


print("--------------------Linked List--------------------")





