class Queue:
    def __init__(self):
        self.items=[]
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items==[]
    
queue=Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeue item:", queue.dequeue())
print("Queue is empty:", queue.is_empty())
