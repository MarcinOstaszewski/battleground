import random
from box import Box

def set_vars():
  vars = Box({
    "name": "Shooter",
    "color": (0, 200, 0),
  })
  return vars

def update(r):
  r.direction += random.uniform(0.1, 0.3)
  r.speed += random.uniform(-30, 30)
  r.move(r.direction, r.speed)
  
  return r