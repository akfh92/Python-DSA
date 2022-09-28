class Node:
    def __init__(self, dataVal=None):
        self.prevVal = None
        self.nextVal = None
        self.dataVal = dataVal
        
        
class dLinkedList:
    def __init__(self):
        self.headVal = None
        

    def prepend(self,val):
        newNode=Node(val)
        if self.headVal == None:
            self.headVal = newNode
            return
        newNode.nextVal = self.headVal
        self.headVal= newNode


    def append(self,val):
        newNode=Node(val)
        if self.headVal == None:
            self.headVal = newNode
            return
        counter = self.headVal
        while counter.nextVal != None:
            counter = counter.nextVal
        counter.nextVal = newNode
        newNode.prevVal = counter
        
        
    def printNode(self):
        if self.headVal is None:
            print("Linked List is Empty!")
            return
        counter = self.headVal
        while counter.nextVal != None:
            print(counter.dataVal, end = " -> ")
            counter=counter.nextVal
        print(counter.dataVal, end=" -> ")
        print("END")

        


        
    def removeFirstNode(self):
        if self.headVal == None:
            print("Linked List is Empty!")
            return
        if self.headVal.nextVal == None:
            self.headVal = None
            return
        self.headVal = self.headVal.nextVal
        self.headVal.prevVal = None

        
    def removeLastElement(self):
        if self.headVal == None:
            print("Empty List")
            return
        if self.headVal.nextVal == None:
            self.headVal = None
            return
        counter = self.headVal
        while counter.nextVal != None:
            counter = counter.nextVal
        
        counter=counter.prevVal
        counter.nextVal = None
            