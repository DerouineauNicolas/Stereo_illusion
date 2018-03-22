from model import RubiksCube, Color
from enum import Enum

def print_face(Face_i):
    print ('-------')  
    print ('|'+Face_i.a.name+'|'+Face_i.b.name+'|'+Face_i.c.name+'|')
    print ('|'+Face_i.d.name+'|'+Face_i.e.name+'|'+Face_i.f.name+'|')
    print ('|'+Face_i.g.name+'|'+Face_i.h.name+'|'+Face_i.i.name+'|')     

def print_cube(Cube_i):
    print ('right')
    print_face(Cube_i.R)
    print ('left')
    print_face(Cube_i.L)
    print ('up')
    print_face(Cube_i.U)
    print ('down')
    print_face(Cube_i.D)
    print ('front')
    print_face(Cube_i.U)
    print ('bottom')
    print_face(Cube_i.B)


