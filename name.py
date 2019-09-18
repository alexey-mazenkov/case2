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


def figure1(x, y, a):
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


def figure2(x, y, a):
    # TODO: (Mikhailov) - нарисуй фигуру 2, чтобы одна сторона с figure1 была одинаковой
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.up()


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
    turtle.right(120)
    turtle.forward(b)
    turtle.right(120)
    turtle.forward(c)
    turtle.right(120)
    turtle.up()


def rectangle():
    # TODO: (Kravtsov) - нарисуй прямоугольник
    pass

def main():
    '''
    Main function.
    :return: None
    '''
    # рисунок 1.
    turtle.hideturtle()
    circle(100,100,100)
    triangle(0, 0, 20, 20, 20)
    figure2(-100, -100, 20)
    figure1(-40, 0, 30)
    turtle.done()


if __name__ == '__main__':
    main()