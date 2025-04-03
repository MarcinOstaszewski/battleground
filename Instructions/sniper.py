import random
from box import Box

def set_vars():
  vars = Box({
    "name": "Sniper",
    "color": (0, 0, 255),
    "max_speed": 90,
  })
  return vars

def update(r):
  r.move(r.direction, r.speed)
  if not r.speed > r.vars.max_speed:
    r.speed += 0.4
    r.direction += random.uniform(0, 0.5)
  else:
    r.speed = 1

  return r
