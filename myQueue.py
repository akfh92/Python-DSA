class MyQueue:
    def __init__(self,size):
        self.queue=list()
        for i in range(0,size):
            self.queue.append(0)
        self.size=size
        self.front = 0
        self.rear = 1
        
    
    def myEnqueue(self,val):
        if self.rear+1 == self.front or (self.rear%self.size) == self.front:
            print("Queue is full")
            return
        if self.rear<self.size:
            self.queue[self.rear] = val
            self.rear += 1
            return
        self.queue[self.rear%self.size] = val
        self.rear = self.rear%self.size
        
    def printMyQueue(self):
        temp = self.front
        while temp!=self.rear:
            if temp == self.size:
                temp%=self.size
            print(self.queue[temp], end=" -> ")
            temp+=1
        print("end")

        