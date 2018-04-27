import random

from simple_plotter.point import Point
from simple_plotter.path import Path
from simple_plotter.svg import save_svg
from simple_plotter.gcode import save_gcode

paper = {
  'width': 320,
  'height': 240,
  'style': '<style>path {stroke: #f09; stroke-weight: 0.5px; fill: none; opactiy: 0.75} path:nth-child(odd) {stroke: #09f; stroke-weight: 0.5px; fill: none; opactiy: 0.75}</style>',
  'paths': []
}

paper['center'] = Point(paper['width'] / 2, paper['height'] / 2)

num_lines = random.randint(50, 100)
shift_skew = random.randint(50, 100)
shift_angle = random.randrange(5)

def wiggle_square(size, num_lines):
  wiggle_points = []

  for p in range(num_lines):
    if p % 2 == 0:
      wiggle_points.append(Point(size / num_lines * p, 0))
      wiggle_points.append(Point(size / num_lines * p + size / shift_skew, size))
    else:
      wiggle_points.append(Point(size / num_lines * p, size))
      wiggle_points.append(Point(size / num_lines * p, 0))

  return Path(wiggle_points)

square_size = 140
square_center = Point(square_size / 2 + 50, square_size / 2 + 50)

wiggle_a = wiggle_square(square_size, num_lines)
wiggle_a.move(50, 50)
wiggle_a.rotate(square_center, random.randint(0, 3) * 90)

wiggle_b = wiggle_a.clone()
wiggle_b.rotate(square_center, random.randint(0, 1) * 180 + shift_angle)


paper['paths'].append(wiggle_a)
paper['paths'].append(wiggle_b)

save_svg(
  filename = 'svgs/wiggle.svg',
  paths = paper['paths'],
  width = paper['width'],
  height = paper['height'],
  style = paper['style']
)

save_gcode(
  filename = 'gcode/wiggle_a.gcode',
  paths = [wiggle_a],
)

save_gcode(
  filename = 'gcode/wiggle_b.gcode',
  paths = [wiggle_b],
)