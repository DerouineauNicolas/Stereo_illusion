from model import RubiksCube, Color
from view import print_cube

cube = RubiksCube(Color.W, Color.Y, Color.O, Color.R, Color.G, Color.B)
print_cube(cube)
