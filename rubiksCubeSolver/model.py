__author__ = 'nderouineau'

from enum import Enum
import random

# ===========================
#
#      [Mvc] Pattern
#
# ===========================

class Color(Enum):
    W   = 1
    Y   = 2
    O   = 3
    R   = 4
    G   = 5
    B   = 6

class Face:
    def __init__(self, input_color):
        self.a = input_color
        self.b = input_color
        self.c = input_color
        self.d = input_color
        self.e = input_color
        self.f = input_color
        self.g = input_color
        self.h = input_color
        self.i = input_color

class RubiksCube:
    def __init__(self,R_color,L_color,U_color,D_color,F_color,B_color):
        self.R = Face(R_color)
        self.L = Face(L_color)
        self.U = Face(U_color)
        self.D = Face(D_color)
        self.F = Face(F_color)
        self.B = Face(B_color)
