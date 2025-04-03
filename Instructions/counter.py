import random

from box import Box

def set_vars():
  vars = Box({
    "name": "Counter",
    "color": (220, 0, 0),
    "scan_direction": 90,
    "scan_width": 5,
  })
  return vars

def update(r):
  scan_result = r.scan(r.vars.scan_direction, r.vars.scan_width)

  r.speed = 3

  r.move(r.direction, r.speed)

  r.direction += 1
  r.vars.scan_direction += r.vars.scan_width / 2
  # if r.vars.scan_direction > 360:
  #   r.vars.scan_direction -= 360

  return r

