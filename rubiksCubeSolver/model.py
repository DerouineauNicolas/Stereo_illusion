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
    def __init__(self):
        self.R = [random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color))]
        self.L = [random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color))]
        self.U = [random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color))]
        self.D = [random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color))]
        self.F = [random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color))]
        self.B = [random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color)), random.choice(list(Color))]

