import turtle
import math
# Plotando o fractal espiral de
# Fibonacci usando o Turtle

def fiboPlot(n):
    a = 0 
    b = 1    
    square_a = a
    square_b = b

    # Selecionando a cor preta da dimensão quadratica
    x.pencolor("black")

    # Formando o primeiro quadrado
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)
    x.left(90)
    x.forward(b * factor)

    #Procesando a serie Fibonacci
    # O tamanho da size == quadrado b, é somada com o quadrado a
    # sendo então que o tamanho size, sera subtituido por um novo square
    size = square_b
    square_b = square_b + square_a
    square_a = size

    #Processar quadrados restantes
    for i in range(1,n):
        x.backward(square_a * factor)
        x.right(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        x.left(90)
        x.forward(square_b * factor)
        #Procesar novamente a serie Fibonacci
        size = square_b
        square_b = square_b + square_a
        square_a = size
    
    #Começar a caneta no ponto spiral
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    #Selecionando a cor da linha amarelo que passa no spiral de Fibonacci
    x.pencolor("yellow")

    #Fibonacci espiral plot
    x.left(90)

    for i in range(n):
        print(b)
        fdwd = math.pi * b * factor / 2
        fdwd /= 90
        for j in range(90):
            x.forward(fdwd)
            x.left(1)
        size = a
        a = b
        b = size + b

# aqui está o 'factor' de multipicação
# o factor vai espantir na escala
factor = 1

n = int(input('Enter the number of iterations (must be > 1): '))

if n > 0:
    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    fiboPlot(n)
    turtle.done()
else:
    print("Number of iterations must be > 0")