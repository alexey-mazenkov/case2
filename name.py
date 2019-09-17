# нарисовать фигуры
# размер окна 1000*1000
# Developers: A.Mazenkov
#             A.Mikhailov
#             K.Kravtsov

import turtle

def square(x, y, a):
    # TODO: (Mikhailov) - нарисуй квадрат
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.up
    turtle.exitonclick()

def circle(x, y, a):
    # TODO: (Mikhailov) - нарисовать круг
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.circle(a)


def figure1(x, y, z):
    # TODO: (Mikhailov) - нарисуй фигуру
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(140)
    turtle.forward(a)
    turtle.right(40)
    turtle.forward(a)
    turtle.right(140)
    turtle.forward(a)
    turtle.right(40)
    turtle.up()
    pass

def figure2():
    # TODO: (Mikhailov) - нарисуй фигуру 2, чтобы одна сторона с figure1 была одинаковой
    pass

def figure3():
    # TODO: (Kravtsov) - нарисуй произвольную фигуру 4

    pass

def figure4():
    # TODO: (Kravtsov) - нарисуй произвольную фигуру 4, чтобы одна сторона с figure3 была одинаковой
    pass

def triangle(x, y, a, b, c):
    # TODO: (Kravtsov) - нарисуй треугольник
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(c)
    turtle.right(135)
    turtle.up()
    pass
def triangle2(x, y, a, b, c):
    # TODO: (Kravtsov) - нарисуй треугольник под другим углом
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(c)
    turtle.right(90)
    turtle.up()
    pass

def triangle3(x, y, a, b, c):
    # TODO: (Kravtsov) - нарисуй треугольник под другим углом
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.left(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(c)
    turtle.up()
    pass

def triangle4(x, y, a, b, c):
    # TODO: (Kravtsov) - нарисуй стреугольник под другим углом
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(135)
    turtle.forward(c)
    turtle.left(135)
    turtle.up()
    pass

def rectangle():
    # TODO: (Kravtsov) - нарисуй прямоугольник
    pass

def main():
    '''
    Main function.
    :return: None
    '''
    # рисунок 1.
    circle(100,100,100)
    
    turtle.done()


if __name__ == '__main__':
    main()