class Queue:
    def __init__(self):
        self.front = None
        self.back = None
    
    def enqueue(self,inputObject):
        newNode = QNode() 
        newNode.setValue(inputObject)
        if self.front is None:
            self.front = newNode
        
        elif self.back is None:    
            self.back = newNode
            self.back.setAhead(self.front)
            self.front.setBehind(self.back)
            
            
        else:
            self.back.setBehind(newNode)
            self.back = newNode
            newNode.setAhead(self.back)

    def dequeue(self):
        if(self.front.getBehind() is not None):
            self.front = self.front.getBehind()
        else:
            self.front = None
            
    def getFront(self):
        return self.front
    def getBack(self):
        return self.back
        
