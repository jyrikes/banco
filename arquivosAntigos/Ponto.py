import math


def distancia(x, xOutro, y, yOutro):
    dist = math.sqrt((xOutro-x)**2 + (yOutro-y)**2)
    return dist


x1 = int(input("digite o valor da coordenada x do ponto 1"))
y1 = int(input("digite o valor da coordenada y do ponto 1"))

x2 = int(input("digite o valor da coordenada x do ponto 2"))
y2 = int(input("digite o valor da coordenada y do ponto 2"))

x3 = int(input("digite o valor da coordenada x do ponto 3"))
y3 = int(input("digite o valor da coordenada y do ponto 3"))

x4 = int(input("digite o valor da coordenada x do ponto 4"))
y4 = int(input("digite o valor da coordenada y do ponto 4"))

dist1 = distancia(x1, x2, y1, y2)
print("distancia do ponto 1 até ponto 2 é", dist1)

dist2 = distancia(x1, x3, y1, y3)
print("distancia do ponto 1 até ponto 3 é", dist2)

dist3 = distancia(x1, x4, y1, y4)
print("distancia do ponto 1 até ponto  é", dist3)
