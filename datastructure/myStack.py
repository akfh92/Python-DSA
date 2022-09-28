class myStack:
    def __init__(self,val=None):
        self.myStack=list()
        if val is not None:
            self.myStack.append(val)
            self.top=1
            return
        self.top=0
        
        
    def printStack(self):
        if self.top == 0 :
            print("---EMPTY STACK---")
            return
        print("---TOP---")
        temp = self.top
        while temp > 0:
            print("   ",self.myStack[temp-1])
            print("---------")
            temp-=1
        print("'\\\\\\\\\\\\\\\\'")
        print("\n\n")
        
        
    def push(self, val):
        if self.top == len(self.myStack):
            self.myStack.append(val)
            self.top+=1
            return
        self.myStack[self.top] = val
        self.top+=1
        
        
    def pop(self):
        print("Popped: ",self.myStack[self.top-1])
        print("\n\n")
        self.top -= 1
        
        
    def size(self):
        print("Size of stack:",self.top)
    
    
    def peak(self):
        print("Peak value: ",self.myStack[self.top-1])