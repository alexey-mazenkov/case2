# нарисовать фигуры
# размер окна 1000*1000
# Developers: A.Mazenkov
#             A.Mikhailov
#             K.Kravtsov

import turtle
import math

t = turtle
m = math

def square(x, y, a, color, right, left):
    # TODO: (Mikhailov) - нарисуй квадрат
    t.up()
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.down()
    t.begin_fill()
    t.color(color)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.end_fill()
    t.up

def circle(x, y, a, color, right, left):
    # TODO: (Mikhailov) - нарисовать круг
    t.up()
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.down()
    t.begin_fill()
    t.color(color)
    t.circle(a)
    t.end_fill()

def figure1(x, y, a, color, right, left):
    # TODO: (Mikhailov) - нарисуй фигуру
    # Ромб.
    t.up()
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.down()
    t.begin_fill()
    t.color(color)
    t.forward(a)
    t.right(140)
    t.forward(a)
    t.right(40)
    t.forward(a)
    t.right(140)
    t.forward(a)
    t.right(40)
    t.end_fill()
    t.up()


def figure2(x, y, a, color, right, left):
    # TODO: (Mikhailov) - нарисуй фигуру 2, чтобы одна сторона с figure1 была одинаковой
    # Параллелограмм
    t.up()
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.down()
    t.begin_fill()
    t.color(color)
    t.forward(a)
    t.right(120)
    t.forward(a)
    t.right(60)
    t.forward(a)
    t.right(120)
    t.forward(a)
    t.end_fill()
    t.up()


def figure3(x, y, a, color, right, left):
    # TODO: (Kravtsov) - нарисуй произвольную фигуру 4
    # Пятиугольник
    t.up()
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.down()
    t.begin_fill()
    t.color(color)
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
    t.end_fill()
    t.up()


def figure4(x, y, a, color, right, left):
    # TODO: (Kravtsov) - нарисуй произвольную фигуру 4, чтобы одна сторона с figure3 была одинаковой
    # Прямоугольный треугольник
    t.up()
    t.setposition(x, y)
    t.down()

    b = (a * m.tan(math.radians(45)))
    c = (a / m.cos(math.radians(45)))

    t.right(right)
    t.left(left)
    t.begin_fill()
    t.color(color)
    t.forward(a)
    t.left(135)
    t.forward(c)
    t.left(135)
    t.forward(b)
    t.end_fill()

def triangle(x, y, a, color, right, left):
    # TODO: (Kravtsov) - нарисуй равносторонний треугольник
    t.up()
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.down()
    t.begin_fill()
    t.color(color)
    t.forward(a)
    t.right(120)
    t.forward(a)
    t.right(120)
    t.forward(a)
    t.right(120)
    t.end_fill()
    t.up()


def rectangle(x, y, a, b, color, right, left):
    # TODO: (Kravtsov) - нарисуй прямоугольник
    t.up()
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.down()
    t.begin_fill()
    t.color(color)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.end_fill()
    t.up()

def leg(x, y, color, right, left):
    t.up()
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.down()
    t.begin_fill()
    t.color(color)
    t.forward(70)
    t.right(110)
    t.forward(50)
    t.right(80)
    t.forward(50)
    t.right(30)
    t.forward(35)
    t.right(105)
    t.forward(28)
    t.end_fill()

def leg2 (x, y, color, right, left):
    t.up()
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.down()
    t.begin_fill()
    t.color(color)
    t.forward(30)
    t.right(20)
    t.forward(40)
    t.left(100)
    t.forward(40)
    t.left(72)
    t.forward(80)
    t.left(115)
    t.forward(65)
    t.end_fill()

def triangle2(x, y, color, right, left) :
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.begin_fill()
    t.color(color)
    t.right(60)
    t.forward(70)
    t.right(156)
    t.forward(129)
    t.right(156)
    t.forward(70)
    t.end_fill()

def ellipse(x, y, r, color, right, left):
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.begin_fill()
    t.color(color)
    turtle.left(45)
    for loop in range(2):  # Draws 2 halves of ellipse
            turtle.circle(r, 90)  # Long curved part
            turtle.circle(r / 2, 90)
    t.end_fill()

def arc(x, y, r, angle, color, right, left):
    t.setposition(x, y)
    t.right(right)
    t.left(left)
    t.color(color)
    t.begin_fill()
    t.circle(r, angle)
    t.end_fill()

def main():
    '''
    Main function.
    :return: None
    '''

    # рисунок 1.
    t.hideturtle()
    figure4(140, 40, 40, 'red', 0, 230)
    rectangle(119, 15, 80, 30, 'blue', 0, 0)
    leg(58, 68, '#F4CD8A', 0, 55)
    figure2(-25, 30, 70, 'black', 35, 0)
    figure2(-9, 40, 70, 'red', 65, 0)
    leg2(-90, 12, '#F4CD8A', 0, 37)
    rectangle(-80, -23, 30, 80, 'red', 0, 74)
    figure4(-160, -18, 40, 'blue', 90, 0)
    figure3(-63, 80, 70, 'orange', 0, 40)
    triangle(0, 175, 70, 'black', 0, 37)
    triangle(-68, 192, 70, 'blue', 0, 73)
    triangle2(-68, 192, 'orange', 0, 0)
    rectangle(-139, 193, 62, 40, 'blue', 0, 100)
    rectangle(23, 231, 60, 40, 'black', 71, 0)
    ellipse(-65, 210, 50, '#F4CD8A', 0, 110)
    rectangle(13, 195, 30, 80, '#F4CD8A', 0, 25)
    arc(90, 173, 20, 100, '#F4CD8A', 51, 0)
    figure2(-135, 140, 30, '#F4CD8A', 0, 140)
    rectangle(-145, 135, 30, 50, '#F4CD8A', 35, 0)
    turtle.done()


if __name__ == '__main__':
    main()