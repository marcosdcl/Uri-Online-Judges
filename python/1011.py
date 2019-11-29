# Sphere

def sphere_vol(radius):
  '''Calculates the volume of a sphere'''
  pi = 3.14159
  radius_cube = radius * radius * radius
  vol = (4 / 3) * pi * radius_cube
  return vol

radius = float(input())
vol = sphere_vol(radius)
print('VOLUME = {:.3f}'.format(vol))
