import random
from box import Box

def set_vars():
  vars = Box({
    "name": "Sniper",
    "color": (0, 0, 255),
    "max_speed": 100,
    "scan_direction": 90,
    "scan_width": 5,
  })
  return vars

def update(r):

  scan_results = r.scan_rich(r.vars.scan_direction, r.vars.scan_width)
  if scan_results and scan_results[0].distance < 1000 and scan_results[0].health > 0:
    print(f"Scan results: {scan_results}")
    r.shoot(r.vars.scan_direction, scan_results[0].distance)

  r.speed = 80

  r.move(r.direction, r.speed)

  if not r.speed > r.vars.max_speed:
    r.speed += 0.4
    r.direction += random.uniform(0, 0.5)
    r.vars.scan_direction += random.uniform(-1, 15)
  else:
    r.speed = 1
    r.vars.scan_direction = 45
    r.direction -= 17

  return r
