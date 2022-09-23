class Node:
    def __init__(self=None, dataVal=None):
        self.prevVal = None
        self.nextVal = None
        self.dataVal = dataVal
        
        
class dLinkedList:
    
    
    def __init__(self,dataVal = None):
        self.headVal = None

    def listPrint(self):
        temp = self.headVal
        while temp.nextVal:
            print(f"{temp.dataVal} --> ", end=" ")
            temp=temp.nextVal
        print(temp.dataVal," --> ",end=" ")
        print("end")
        
        

        

    def prepend(self,val):
        newNode = Node(val)
        temp = self.headVal
        temp.prevVal = newNode
        self.headVal = temp.prevVal


    def append(self,val):
        newNode=Node(val)
        if self.headVal == None:
            self.headVal = newNode
            return
        temp = self.headVal
        while temp.nextVal:
            temp=temp.nextVal
        temp.nextVal = newNode
        
        

        
        
#     def insertBetween(self,idx,val):


        
#     def removeFirstNode(self):

        
#     def removeKeyElement(self,key):

        