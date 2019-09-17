# нарисовать фигуры
# размер окна 1000*1000
# Developers: A.Mazenkov
#             A.Mikhailov
#             K.Kravtsov

import turtle

def square(x, y, a):
    # TODO: (Mikhailov) - нарисуй квадрат
    turtle.up()
    turtle.setposition(x,y)
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

def circle():
    # TODO: (Mikhailov) - нарисовать круг
    pass

def figure1():
    # TODO: (Mikhailov) - нарисуй фигуру
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

def triangle():
    # TODO: (Kravtsov) - нарисуй треугольник
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
    square(100,100,100)

    turtle.done()


if __name__ == '__main__':
    main()