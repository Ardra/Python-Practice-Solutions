class reverse_iter:
     def __init__(self, list):
             self.list = list
     def __iter__(self):
             return self
     def next(self):
             while(True):
                     if len(self.list)> 0:
                             return self.list.pop()
                     else:
                             raise StopIteration()
 
