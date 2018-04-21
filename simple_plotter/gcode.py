def get_gcode_path(path):
  gcode = '\n'

  for i, p in enumerate(path.points):
    gcode += '\nG1 X{} Y{}'.format(p.x, p.y)

    if i == 0:
      gcode += '\nM03 S1000'

  if path.closed == True: 
    gcode += '\nG1 X{} Y{}'.format(path.points[0].x, path.points[0].y)

  gcode += '\nM05 S1000'

  return gcode

def save_gcode(filename, paths):
  gcode = 'F10000\nM05 S1000\nG1 X0 Y0'

  for p in paths:
    gcode += get_gcode_path(p)

  gcode += '\n\nM05 S1000\nG1 X0 Y0'

  f = open(filename, 'w')
  f.write(gcode)
  f.close()
  
  print(filename + ' saved')