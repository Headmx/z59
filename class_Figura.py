import math
class Figura:
    def __init__(self,a,b,*args):
        self.a = a
        self.b = b
        print ( 'hello __init__')
class Pryamougolnik(Figura) :
    def perimetr(self):
        print('hello  Pryamougolnik')
        return print((self.a +self.b)*2)
    def square(self):
        print('hello square Pryamougolnik')
        return print (self.a *self.b)
class Kvadrat(Pryamougolnik) :
    def __init__(self, a, *args):
        print ('hello Kvadrat')
        super().__init__(a,a)

class Krug (Figura):
    def __init__(self, d, *args):
        self.d = d
    def perimetr (self):
        return print(math.pi*self.d)
    def square (self):
        return print ((math.pi*self.d**2)/4)
class Romb (Kvadrat):
    def __init__(self, a,b,h,*args):
        self.h = h
        super().__init__(a,b)
        self.b =self.a
        print ('print init Romb')
    def square(self):
        return print (self.a*self.h)
class Chetirehug (Figura):
    def __init__(self,a,b,c,f,*args):
        self.c = c
        self.f = f
        super().__init__(a,b,*args)
    def perimetr(self):
        print('hello 4 perimetr')
        return self.a + self.b + self.c + self.f
    def square(self):
        print ('hello 4 S')
        return print(((self.perimetr()/2 - self.a)*(self.perimetr()/2 - self.b)*(self.perimetr()/2 - self.c)*(self.perimetr()/2 - self.f))**0.5)
class Treugolnik (Figura):
    def __init__(self,a,b,c,*args):
        self.c = c
        super().__init__(a,b,*args)
    def perimetr(self):
        return self.a+self.b+self.c
    def square(self):
        print('hello 3 ug')
        return print (((self.perimetr()/2*((self.perimetr() / 2 - self.a) * (self.perimetr() / 2 - self.b) * (self.perimetr() / 2 - self.c))) ** 0.5))
class Bedr_treugolnik (Treugolnik):
    def __init__(self,a,b,*args):
        super().__init__(a,b,b)
class Ravno_treugolnik (Bedr_treugolnik):
    def __init__(self,a,*args):
        super().__init__(a,a)
class Oval (Figura):
    def __init__(self, d, D, *args):
        self.d = d
        self.D = D
    def square(self):
        return print(math.pi*self.d*self.D/4)
    def perimetr(self):
        return 2*math.pi((self.d**2 + self.D**2)/8)**0.5

# primeri
    abddd = Kvadrat(9,12)
    abddd.square()
    kr = Krug (16)
    kr.square()
    rom = Romb(10,5,7)
    rom.square()
    chet = Chetirehug(11,5,8,7)
    chet.perimetr()
    treug = Ravno_treugolnik(4,8,14)
    treug.square()
    ov = Oval(8,14)
    ov.perimetr()