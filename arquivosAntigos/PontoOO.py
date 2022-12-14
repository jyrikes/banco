import math


class Ponto():

    def __init__(self, xNovo, yNovo):
        self.x = xNovo
        self.y = yNovo

    def distancia(self, outroPonto):
        dist = math.sqrt((outroPonto.x-self.x)**2 + (outroPonto.y-self.y)**2)
        return dist

    def quadrante(self):
        if self.x >= 0 and self.y >= 0:
            return "primeiro quadrante"
        elif self.x < 0 and self.y > 0:
            return "segundo quadrante"
        elif self.x < 0 and self.y < 0:
            return "terceiro quadrante"
        else:
            return "quarto quadrante"


class Circuferencia():

    def __init__(self, p, raio):
        self.centro = p
        self.r = raio

    def pertence(self, p):
        if self.centro.distancia(p) <= self.r:
            return True
        else:
            return False


p = Ponto(1, 1)
x2 = int(input("digite o x do ponto 2:"))
y2 = int(input("digite o y do ponto 2:"))
p2 = Ponto(x2, y2)

num = 10

dist = p.distancia(p2)
print(dist)
print(p.quadrante())
print(p2.quadrante())

c = Circuferencia(p, 1)
respo = c.pertence(p2)
print(respo)
