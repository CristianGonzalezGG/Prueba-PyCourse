class A:
    def hablar(self):
        print("Esto es A")

class B(A):
    def hablar(self):
        print("Esto es B")

class C(A):
    def hablar(self):
        print("Esto es C")
    
class D(C,B):
    def hablar(self):
        print("Esto es D")

d = D()

d.hablar()