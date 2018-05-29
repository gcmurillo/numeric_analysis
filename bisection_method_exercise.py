from math import *
from sympy import *

a = 2
R = 12
h = 30
theta = 0
W = 100
L = 80

ecuacion = 2*a*pow(R,3)*(((h*pow(sin(theta),3))/3) -
                          ((R*cos(theta)*pow(sin(theta),3))/3) +
                          ((R*theta)/8) - ((R*sin(4*theta))/32) -
                          ((h*theta*cos(theta))/2) +
                          ((h*cos(theta)*sin(2*theta))/4)) - W*L

def biseccion(f, a, b, e):
    '''
    Calcular una raiz r real de la ecuacion f(x) = 0. f es continua en el intervalo [a, b]
    tal que f(a) y f(b) tienen signos diferentes
    :param f: ecuacion
    :param a: intervalo inferior
    :param b: intervalo superir
    :param e: error
    :return:
    '''

    while b - a >= e:
        c = (a+b)/2
        if f(c) == 0:
            return c
        else:
            if f(a) * f(c) > 0:
                a = c
            else:
                b = c
    return c

def f(theta) : return 2*2*pow(12,3)*(((25*pow(sin(theta),3))/3) -
                                                   ((12*cos(theta)*pow(sin(theta),3))/3) +
                                                   ((12*theta)/8) - ((12*sin(4*theta))/32) -
                                                   ((30*theta*cos(theta))/2) +
                                                   ((30*cos(theta)*sin(2*theta))/4)) - 100*80

c = biseccion(f, 0, 2, 0.000001)
print(c)
