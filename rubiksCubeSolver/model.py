__author__ = 'nderouineau'

from enum import Enum
import random

# ===========================
#
#      [Mvc] Pattern
#
# ===========================

class Color:
    White  = 1
    Yellow = 2
    Orange = 3
    Red    = 4
    Green  = 5
    Blue   = 6

class RubiksCube:
    def __init__(self,R_color,L_color,U_color,D_color,F_color,B_color):
        self.R = [R_color,R_color,R_color,R_color,R_color,R_color,R_color,R_color,R_color]
        self.L = [L_color,L_color,L_color,L_color,L_color,L_color,L_color,L_color,L_color]
        self.U = [U_color,U_color,U_color,U_color,U_color,U_color,U_color,U_color,U_color]
        self.D = [D_color,D_color,D_color,D_color,D_color,D_color,D_color,D_color,D_color]
        self.F = [F_color,F_color,F_color,F_color,F_color,F_color,F_color,F_color,F_color]
        self.B = [B_color,B_color,B_color,B_color,B_color,B_color,B_color,B_color,B_color]

