#Node class: this was provided via boardworks in lecture.
class Node: 
    
    #Only the constructor is needed for the node since you only need an entry.
    def __init__(self, entry):
         self.entry = entry
         self.next = None

#Stack class: this was provided via boardworks in lecture.
class Stack: 
    
    #Constructor sets an empty top node.
    def __init__(self):
        self._top = None

    #Boolean method to check if the top node is empty.
    def is_empty(self):
        return self._top == None

    #Push method to add a new node to the top
    def push(self, entry):
        if self.is_empty == True:
            self._top == Node(entry)
        else:
            temp = self._top
            self._top = Node(entry)
            self._top.next = temp

    #Pop method to remove the top node. If it's empty, an exception is raised.
    def pop(self):
        if self._top != None: 
            self._top = self._top.next
        else:
            raise RuntimeError('\n Stack empty!')
    
    #Peek method to check the top node's value. If it's empty, an exception is raised.
    def peek(self):
        if self._top != None:
            return self._top.entry
        else: 
            raise RuntimeError('\n Stack empty!')

#Queue class: this was provided via boardworks in lecture.
class Queue:
    
    #Constructor creates empty front and back nodes. 
    def __init__(self):
        self._front = None
        self._back = None
        
    '''    
    Dequeue method to remove the front node. 
    If the front node is empty, an exception is raised. 
    If the front is the same as the back, both are set to empty values. 
    '''    

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError('\n Queue empty!')
        elif self._front == self._back:
            temp = self._front
            self._front = None 
            self._back = None
            return temp.entry
        else:
            temp = self._front
            self._front = self._front.next
            return temp.entry
    
    #Enqueue method to add a node to the back.
    def enqueue(self, entry):
        temp = Node(entry)
        if self.is_empty():
            self._front = Node(entry)
            self._back = self._front 
        else:
            self._back.next = temp 
            self._back = temp
            
    #Boolean method to check if the queue is empty.        
    def is_empty(self):
        return self._front == None
     
    #Peek method to return the node at the front of the queue. If it's empty, an exception is raised.  
    def peek(self):
        if self._front != None:
            return self._front.entry
        else:
            raise RuntimeError('\n Queue empty!')
            

#New data structure learned in lecture on Monday, February 21st.
class LinkedList:
    
    #Constructor setting the front node to null while the length is defaulted to 0 of index length.
    def __init__(self):
        self._front = None
        self._length = 0 
    
    def get_length(self):
        return self._length
            
    def get_entry(self, index):
        if (index < 0 or index >= self._length):
            raise RuntimeError("Index out of range! \n")
        else:
            temp_jumper = self._front
            for i in range(0, index):
                temp_jumper = temp_jumper.next
            return temp_jumper.entry
    
    def insert(self, index, entry):
        newNode = Node(entry)
        if index == 0:
            temp = self._front
            self._front = newNode
            self._front.next = temp
            
            self._length += 1
        elif 0 < index < self._length:
            temp = self.getNode(index)
            before = self.getNode(index-1)
            before.next = newNode
            newNode.next = temp
            
            self._length += 1
        elif index == self._length:
            jumper = self.getNode(index-1)
            jumper.next = newNode
            
            self._length += 1
        else:
            raise RuntimeError("Index is out of bounds! \n")
    
    def getNode(self, index):
        jumper = self._front 
        for i in range(0, index):
            jumper = jumper.next
        return jumper
    
    def set_entry(self, index, entry):
      if not (0 <= index <= (self._length - 1)):
        raise RuntimeError("Index out of bounds! \n")
      self.remove(index)
      self.insert(index, entry)
        
    
    def remove(self, index):
        if 0 < index < (self._length-1):
            before = self.getNode(index-1)
            after = self.getNode(index+1)
            target = self.get_entry(index)
            before.next = after
            
            self._length -= 1
            return target
        elif(index == self._length-1):
            before = self.getNode(index-1)
            target = self.get_entry(index)
            before.next = None
            
            self._length -= 1
            return target
        elif(index == 0):
            after = self.getNode(index + 1)
            target = self.get_entry(index)
            self._front = after
            
            self._length -= 1
            return target
        else:
            raise RuntimeError("Index is out of bounds! \n")
            
    def clear(self):
        for i in range(0, self._length):
            self.remove(0)
            