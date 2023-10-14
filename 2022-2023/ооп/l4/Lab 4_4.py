class Stack:
    def __init__(self):
        self.values = []


    def push(self, item):
        self.values.insert(0, item)


    def pop(self):
        if not self.values:
            print('Empty Stack')
        else:
            # tmp = self.values[0]
            #   del self.values[0]
            # return tmp
            return self.values.pop(0)
            
    
    def peek(self):
        if not self.values:
            print('Empty Stack')
            return None
        else:
            return self.values[0]
            
    
    def is_empty(self):
        if not self.values:
            return True
        else:
            print(self.values)
            return False

    
    def size(self):
        return len(self.values)


s = Stack() 
s.peek()  # распечатает 'Empty Stack' 
print(s.is_empty())  # распечатает True 
s.push('cat')  # кладем элемент 'cat' на вершину стека 
s.push('dog')  # кладем элемент 'dog' на вершину стека 
print(s.peek())  # распечатает 'dog' 
s.push(True)  # кладем элемент True на вершину стека 
print(s.size())  # распечатает 3 
print(s.is_empty())  # распечатает False 
s.push(777)  # кладем элемент 777 на вершину стека 
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его 
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его 
print(s.size())  # распечатает 2 