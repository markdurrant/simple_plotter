def get_svg_path(path, document_height):
  svg_path = ""

  for i, point in enumerate(path.points):
    if i == 0:
      svg_path += "M "
    else:
      svg_path += " L"

    # Use document height to flip Y coordinates
    svg_path += str(point.x) + " " + str(document_height - point.y)

  if path.closed == True:
    svg_path += " Z"

  return '<path d="' + svg_path + '"/>'

def save_svg(filename, paths, width, height, style):
  svg = '<?xml version="1.0" encoding="utf-8"?>' \
        '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" ' \
        'xmlns:xlink="http://www.w3.org/1999/xlink" ' \
        'width="{}" height="{}" viewbox="0 0 {} {}">{}' \
        .format(width, height, width, height, style)
  
  for p in paths:
    svg += get_svg_path(p, height)
    
  svg += '</svg>'

  f = open(filename, 'w')
  f.write(svg)
  f.close()
  
  print(filename + ' saved')
