
# question3 

class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,c2):
        return complex(self.r + c1.r,self.i+c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}"
    
c1 = complex(1,5)
c2 = complex(6,9)
print(c1+c2)
    
