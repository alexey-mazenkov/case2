# нарисовать фигуры
# размер окна 1000*1000
# Developers: A.Mazenkov
#             A.Mikhailov
#             K.Kravtsov

import turtle
import math

t = turtle
m = math

def square(x, y, a):
    # TODO: (Mikhailov) - нарисуй квадрат
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.up

def circle(x, y, a):
    # TODO: (Mikhailov) - нарисовать круг
    t.up()
    t.setposition(x, y)
    t.down()
    t.circle(a)


def figure1(x, y, a):
    # TODO: (Mikhailov) - нарисуй фигуру
    # Ромб.
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(140)
    t.forward(a)
    t.right(40)
    t.forward(a)
    t.right(140)
    t.forward(a)
    t.right(40)
    t.up()


def figure2(x, y, a):
    # TODO: (Mikhailov) - нарисуй фигуру 2, чтобы одна сторона с figure1 была одинаковой
    # Параллелограмм
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(120)
    t.forward(a)
    t.right(60)
    t.forward(a)
    t.right(120)
    t.forward(a)
    t.up()


def figure3(x, y, a):
    # TODO: (Kravtsov) - нарисуй произвольную фигуру 4
    # Пятиугольник
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(72)
    t.forward(a)
    t.right(72)
    t.forward(a)
    t.right(72)
    t.forward(a)
    t.right(72)
    t.forward(a)
    t.right(72)
    t.up()


def figure4(x, y, a):
    # TODO: (Kravtsov) - нарисуй произвольную фигуру 4, чтобы одна сторона с figure3 была одинаковой
    # Прямоугольный треугольник
    t.up()
    t.setposition(x, y)
    t.down()

    b = (a * m.tan(math.radians(45)))
    c = (a / m.cos(math.radians(45)))

    t.forward(a)
    t.left(135)
    t.forward(c)
    t.left(135)
    t.forward(b)

def triangle(x, y, a):
    # TODO: (Kravtsov) - нарисуй равносторонний треугольник
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(120)
    t.forward(a)
    t.right(120)
    t.forward(a)
    t.right(120)
    t.up()


def rectangle(x, y, a, b):
    # TODO: (Kravtsov) - нарисуй прямоугольник
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.up()

def leg(x,y):
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(70)
    t.right(110)
    t.forward(50)
    t.right(80)
    t.forward(50)
    t.right(30)
    t.forward(35)
    t.right(105)
    t.forward(28)

def leg2 (x, y):
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(30)
    t.right(20)
    t.forward(40)
    t.left(100)
    t.forward(40)
    t.left(72)
    t.forward(80)
    t.left(115)
    t.forward(65)

def main():
    '''
    Main function.
    :return: None
    '''

    # рисунок 1.
    t.hideturtle()
    t.color('red')
    t.begin_fill()
    t.left(230)
    figure4(140, 40, 40)
    t.end_fill()
    t.begin_fill()
    t.color('blue')
    rectangle(119, 15, 80, 30)
    t.end_fill()
    t.left(55)
    t.begin_fill()
    t.color('#F4CD8A')
    t.begin_fill()
    leg(58, 68)
    t.end_fill()
    t.color('black')
    t.begin_fill()
    t.right(35)
    figure2(-25, 30, 70)
    t.end_fill()
    t.begin_fill()
    t.color('red')
    t.right(65)
    figure2(-9, 40, 70)
    t.end_fill()
    t.left(37)
    t.begin_fill()
    t.color('#F4CD8A')
    leg2(-90, 12)
    t.end_fill()
    t.left(74)
    t.begin_fill()
    t.color('red')
    rectangle(-80, -23, 30, 80)
    t.end_fill()
    t.begin_fill()
    t.color('blue')
    t.right(90)
    figure4(-160, -18, 40)
    t.end_fill()
    t.left(40)
    t.begin_fill()
    t.color('orange')
    figure3(-63, 80, 70)
    t.end_fill()
    turtle.done()


if __name__ == '__main__':
    main()