class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
            return str(self.value)
        
class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def append(self, value):
        nuevo_nodo = Nodo(value)
        if self.size==0:
            self.first = nuevo_nodo

        else:
            actual=self.first
            while actual.next != None:
                actual=actual.next
            actual.next=nuevo_nodo
        self.size+=1    
        return nuevo_nodo
    def get_first(self):
        return self.first   
    
    def remove(self, value):
        if self.size==0:
            return False
        actual=self.first
        try:
            while actual.value != value:
                actual=actual.next

            nodo_saliente=actual.next
            actual.next=nodo_saliente.next
        except AttributeError:
            return False    
        self.size-=1
        return nodo_saliente
    
    def __len__(self):
        return self.size    
    
    def __str__(self):
        string="["
        actual=self.first
        while actual != None:
            string+=str(actual)
            string+=str(",")
            actual=actual.next
        string+="]"
        return string
Mylist=LinkedList()
Mylist.append(100)
Mylist.append("z")
Mylist.append("tres")
Mylist.append(250)
Mylist.append("hola")
print(Mylist)