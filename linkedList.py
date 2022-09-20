class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal
        self.nextVal = None

class SLinkedList:
    def __init__(self):
        self.headVal = Node()
        

    def listPrint(self):
        printVal = self.headVal
        while printVal:
            print(f"{printVal.dataVal} ->",end=" ")
            printVal= printVal.nextVal
        print("End")
        

    def prepend(self,val):
        
        newNode = Node(val)
        newNode.nextVal = self.headVal
        self.headVal = newNode
        

    def append(self,val):
        trackingNode = self.headVal
        if trackingNode.dataVal == None:
            trackingNode.dataVal = val
            return
        while trackingNode.nextVal:
            trackingNode = trackingNode.nextVal
        newNode = Node(val)
        trackingNode.nextVal = newNode
        
        
    def insertBetween(self,idx,val):
        newNode = Node(val)
        trackingNode = self.headVal
        for i in range(1,idx-1):
            trackingNode = trackingNode.nextVal
        newNode.nextVal = trackingNode.nextVal
        trackingNode.nextVal = newNode

        
    def removeFirstNode(self):
        if self.headVal == None:
            return
        self.headVal = self.headVal.nextVal
        
    def removeKeyElement(self,key):
        if self.headVal is None:
            return
        tempNode = self.headVal
        while tempNode.nextVal.dataVal != key:
            tempNode = tempNode.nextVal
            if tempNode.nextVal is None:
                print("That node does not exist in the linked list.")
                return
        tempNode.nextVal = tempNode.nextVal.nextVal