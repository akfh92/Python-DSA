class MyQueue:
    def __init__(self,size):
        self.queue = [["EmptyElement"] for i in range(size)]
        self.size = size
        self.front = 0
        self.rear = 0
        self.currentSize = 0
    
    
    def myEnqueue(self,val):
        if self.isFull():
            print("error: the queue is full.")       
            return
        self.queue[self.rear%self.size] = val
        self.rear= self.rear%self.size+1
        self.currentSize+=1
        
        
    def isFull(self):
        return self.currentSize == self.size
    
    
    def isEmpty(self):
        return self.currentSize == 0
    
    
    def myDequeue(self):
        if self.isEmpty():
            print("error the queue is Empty.")       
            return
        print(f"{self.queue[self.front]} has been dequeued.")
        self.queue[self.front] = "EmptyElement"
        self.front = self.front%(self.size-1)+1
        self.currentSize-=1
        
        
    def printMyQueue(self):
        temp = 0
        while temp<self.size:
            print(self.queue[temp],end=" -> ")
            temp = temp%self.size+1
        print("end")