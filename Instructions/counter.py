import random

from box import Box

def set_vars():
  vars = Box({
    "name": "Counter",
    "color": (220, 0, 0),
    "secondary_color": (180, 0, 0),
    "scan_direction": 90,
    "scan_width": 5,
  })
  return vars

def update(r):
  scan_result = r.scan_rich(r.vars.scan_direction, r.vars.scan_width)

  r.speed = 100

  r.move(r.direction, r.speed)

  r.direction += 1
  r.vars.scan_direction += r.vars.scan_width / 2
  
  if r.vars.scan_direction > 360:
    r.vars.scan_direction -= 360

  return r

