class heap:
    def __init__(self,lst):
        self.heap = lst.sort()
    
    def add(self,i):
        n = len(self.heap)
        self.heap.append(i)
        while self.heap[n] < self.heap((n-1)//2):
            self.heap[n], self.heap[(n-1)//2] = self.heap[(n-1)//2], self.heap[n]
            n = (n-1)//2
            
    def extractmin(self)
        