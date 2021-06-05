#def greeting():
  # print('Hello, World')
#   print('This is fun!')

# greeting()

#give python access to the turtle library
import turtle

def draw_a_line():
  """Draw a line 50 pixels long"""

  turtle.forward(50)

# draw_a_line()

def draw_a_L():
  '''Draw a backwards L.'''

  turtle.forward(50)
  turtle.left(90)
  turtle.forward(100)

#draw_a_L()

def draw_a_funky_S():
  '''Draw a funky S'''

  turtle.forward(50)
  turtle.left(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(50)

#draw_a_funky_S()

def draw_a_square():
  '''Draw a square'''

  turtle.forward(40)
  turtle.left(90)
  turtle.forward(40)
  turtle.left(90)
  turtle.forward(40)
  turtle.left(90)
  turtle.forward(40)

#draw_a_square()

def draw_a_rectangle():
  '''Draw a rectangle'''

  turtle.forward(80)
  turtle.left(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(80)
  turtle.left(90)
  turtle.forward(20)

# draw_a_rectangle()

def draw_a_triangle():
  '''Draw a triangle'''

  turtle.left(60)
  turtle.forward(50)

  turtle.right(120)
  turtle.forward(50)

  turtle.right(120)
  turtle.forward(50)

# draw_a_triangle()

def draw_a_line_w_var():
  '''Draw a line 50 pixels long using a variable'''

  length=50
  turtle.forward(length)

# draw_a_line_w_var()

def draw_a_square_w_var():
  '''Draw a square using variables'''

  length=40
  angle=90
  turtle.forward(length)
  turtle.left(angle)
  turtle.forward(length)
  turtle.left(angle)
  turtle.forward(length)
  turtle.left(angle)
  turtle.forward(length)

# draw_a_square_w_var()

def draw_a_spiral():
    """Draw a spiral."""

    right_angle = 90
    length = 5

    turtle_color= "green"
    turtle.color=(turtle_color)

    turtle.forward(length)
    turtle.left(right_angle)
    length = length + 0

    turtle.forward(length)
    turtle.left(right_angle)
    length = length + 5

    turtle.forward(length)
    turtle.left(right_angle)
    length = length + 5

    turtle.forward(length)
    turtle.left(right_angle)
    length = length + 10

    turtle.forward(length)
    turtle.left(right_angle)
    length = length + 15

    turtle.forward(length)
    turtle.left(right_angle)
    length = length + 25

    turtle.forward(length)
    turtle.left(right_angle)
    length = length + 40

    turtle.forward(length)
    turtle.left(right_angle)
    length = length + 65

    turtle.forward(length)
    turtle.left(right_angle)

# draw_a_spiral()

def draw_a_square_with_while():
  '''Draw a square using a while loop'''

  right_angle = 90
  length = 150
  num_sides=4

  i=0

  while i < num_sides:
    if i==3:
      turtle.color("red")

    turtle.forward(length)
    turtle.left(right_angle)
    i=i+1

    #all dont; change color back now
    turtle.color("black")

# draw_a_square_with_while()

def draw_a_rectangle_with_loop():
  '''Draw a rectangle using a while loop'''

  right_angle=90
  length=150
  num_sides=4
  i=0

  while i< num_sides:
    if (i%2) ==0:
      turtle.forward(length)

    else:
      turtle.forward(length/2)

    turtle.left(right_angle)
    i = i+1

# draw_a_rectangle_with_loop()

def draw_a_hexagon():
  '''Draw a hexagon'''

  length = 100
  num_sides =10
  angle = 360.0 / num_sides

  i = 0

  while i < num_sides:
    turtle.forward(length)
    turtle.left(angle)
    i = i+1

draw_a_hexagon()