import random

from box import Box

def set_vars():
  vars = Box({
    "name": "Counter",
    "color": (220, 0, 0),
    "secondary_color": (180, 0, 0),
    "scan_direction": 90,
    "screen_width": 0,
    "screen_height": 0,
    "scan_width": 5,
  })
  return vars

def update(r):
  if r.vars.screen_width == 0:
    r.vars.screen_width = r.screen.get_width()
    # r.vars.screen_height = r.screen.get_height()

  distance = r.scan(r.vars.scan_direction, r.vars.scan_width)
  if distance < r.vars.screen_width * 0.8:
    r.shoot(r.vars.scan_direction, distance)

  r.speed = 100

  r.move(r.direction, r.speed)

  r.direction += random.uniform(0.6, 3)
  r.vars.scan_direction += r.vars.scan_width / 2
  
  if r.vars.scan_direction > 360:
    r.vars.scan_direction -= 360

  return r

