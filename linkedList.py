class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal
        self.nextVal = None

class SLinkedList:
    def __init__(self):
        self.headVal = None

    def listPrint(self):
        printVal = self.headVal
        while printVal != None:
            print(printVal)
            # print(f"{printVal} ->",end=" ")
            print("End")
            printVal= printVal.nextVal

    def prepend(self,val):
        
        newNode = Node(val)
        newNode.nextVal = self.headVal
        self.headVal = newNode

    def append(self,val):
        print(val)
        trackingNode = self.headVal
        if trackingNode == None:
            trackingNode = val
            return
        while trackingNode.next:
            trackingNode = trackingNode.nextVal
        newNode = Node(val)
        trackingNode.nextVal = newNode
    # def insertBetween(self,idx,val):
