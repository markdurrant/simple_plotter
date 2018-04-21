# Simple plotter

Simple Python 3 tool to generate SVGs and Gcode for the EleksDraw plotter.

#### Example drawing script

```python
from simple_plotter.point import Point
from simple_plotter.path import Path
from simple_plotter.svg import save_svg
from simple_plotter.gcode import save_gcode

# Setup 

paper = {
  'width': 320,
  'height': 240,
  'style': '<style>* {stroke: #09f; stroke-weight: 2px; fill: none;}</style>',
  'paths': []
}

paper['center'] = Point(paper['width'] / 2, paper['height'] / 2)

# ---

# Drawing goes here 

outline = Path([
  Point(0, 0),
  Point(paper['width'], 0),
  Point(paper['width'], paper['height']),
  Point(0, paper['height']),
], closed = True)
paper['paths'].append(outline)

arrow = Path([
  paper['center'].clone().move(0, 20),
  paper['center'].clone().move(20, -20),
  paper['center'].clone().move(-20, -20),
], closed = True)
paper['paths'].append(arrow)

# ---

# Save SVG & Gcode

save_svg(
  filename = 'svgs/example.svg',
  paths = paper['paths'],
  width = paper['width'],
  height = paper['height'],
  style = paper['style']
)

save_gcode(
  filename = 'gcode/example.gcode',
  paths = paper['paths'],
)```


