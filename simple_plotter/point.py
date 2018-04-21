import math
import copy

class Point():
  
  def __init__(self, x = 0, y = 0):
    self.label = "Point"
    self.x = x
    self.y = y
   
  # Move Point by X & Y
  def move(cls, x = 0, y = 0):
    cls.x += x
    cls.y += y
    
    return cls

  # Move Point along a vector
  def move_vector(cls, direction = 0, length = 0):
    # Make 0deg 'North'
    angle = math.radians(direction + 90)

    cls.x += math.cos(angle) * length
    cls.y += math.sin(angle) * length
    
    return cls

  # Roate around another Point
  def rotate(cls, origin, angle):
    radians = math.radians(angle)

    x1 = cls.x - origin.x
    y1 = cls.y - origin.y

    x2 = x1 * math.cos(radians) - y1 * math.sin(radians)
    y2 = x1 * math.sin(radians) + y1 * math.cos(radians)

    cls.x = x2 + origin.x
    cls.y = y2 + origin.y
    
    return cls
    
  # Get the distance to another Point  
  def get_distance_to(cls, point):
    a = cls.x - point.x
    b = cls.y - point.y

    if a == 0:
      distance = b
    elif b == 0:
      distance = a
    else:
      distance = math.fabs(math.sqrt(a * a + b * b))

    return abs(distance)

  # Get the angle to another point
  def get_angle_to(cls, point):
    a = cls.x - point.x
    b = cls.y - point.y

    angle = math.degrees(math.atan2(b, a))

    if angle < 0:
      angle += 360

    # Make 0deg 'North'
    angle += 90

    if angle < 0:
      angle += 360

    return angle

  # Check if one Point is equal to another 
  def is_equal_to(cls, point):
    if cls.x == point.x and cls.y == point.y:
      return True
    else:
      return False

  # Create a clone of the Point
  def clone(cls):
    return copy.deepcopy(cls)

  # Create string of Point info
  def get_log(cls):
    return "\u2022 Point [ x = {}, y = {} ]".format(cls.x, cls.y)

  # Print Point info
  def log(cls):
    print(cls.get_log())
