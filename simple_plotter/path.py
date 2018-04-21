import textwrap
import copy

from simple_plotter.point import Point

class Path():

  def __init__(self, points = [], closed = False):
    self.label = "Path"
    self.points = points
    self.closed = closed

  # Close the Path
  def make_closed(cls):
    cls.closed = True
    
    return cls

  # Open the Path
  def make_open(cls):
    cls.closed = False
    
    return cls

  # Move the Path along X & Y
  def move(cls, x, y):
    for point in cls.points:
      point.move(x, y)
    
    return cls

  # Move the Path along a vector
  def move_vector(cls, direction, length):
    for point in cls.points:
      point.move_vector(direction, length)

    return cls

  # Rotate the Path around a Point
  def rotate(cls, origin, angle):
    for point in cls.points:
      point.rotate(origin, angle)

    return cls
    
  # Scale the Path by a given factor
  def scale(cls, factor):
    for point in cls.points:
      direction = cls.center.get_angle_to(point)
      length = cls.center.get_distance_to(point)
      
      point.move_vector(direction, length * factor - length)      
    
    return cls
    
  # Get the total lenght of the Path
  def get_length(cls):
    length = 0
    
    for i, point in enumerate(cls.points[: -1]):
      length += point.get_distance_to(cls.points[i + 1])
      
    if cls.closed == True:
      length += cls.points[-1].get_distance_to(cls.points[0])  
    
    return length

  # Create a clone of the Path
  def clone(cls):
    return copy.deepcopy(cls)

  # Create a string of Path & child Points info
  def get_log(cls):
    log = "\u2B20  Path [ closed = {} ]".format(cls.closed)
    pointLog = ""

    for i, point in enumerate(cls.points):
      pointLog += "\n" + point.get_log().replace("Point", "Point[" + str(i) + "]")

    return log + textwrap.indent(pointLog, "  ")

  # Print Path & child Points info
  def log(cls):
    print(cls.get_log())
