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


def figure4(x, y, a, c):
    # TODO: (Kravtsov) - нарисуй произвольную фигуру 4, чтобы одна сторона с figure3 была одинаковой
    # Прямоугольный треугольник
    t.up()
    t.setposition(x, y)
    t.down()
    t.forward(a)
    t.right(135)
    t.forward(m.sqrt(a ** 2 + c ** 2))
    t.right(135)
    t.forward(c)
    t.right(135)
    t.up()


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


def main():
    '''
    Main function.
    :return: None
    '''
    # рисунок 1.
    t.hideturtle()
    figure4(40, 70, 70, 70)
    turtle.done()


if __name__ == '__main__':
    main()