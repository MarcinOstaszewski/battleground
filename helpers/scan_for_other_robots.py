import math
from box import Box

def scan_for_other_robots(myself, angle, angle_range, pygame, is_simple_scan):
  angle_range = min(30, angle_range)  # Ensure a maximum angle range of 30 degrees
  robots = myself.get_all_robots_from_state()
  detected_robots = []
  closest_robot_distance = float('inf')

  # Calculate the vertices of the triangular scan area
  tip = myself.position
  left_angle = math.radians(angle - angle_range / 2)
  right_angle = math.radians(angle + angle_range / 2)
  left_vertex = (
    tip[0] + 3000 * math.cos(left_angle),
    tip[1] + 3000 * math.sin(left_angle)
  )
  right_vertex = (
    tip[0] + 3000 * math.cos(right_angle),
    tip[1] + 3000 * math.sin(right_angle)
  )

  # Check if each robot is within the triangular area
  for other_robot in robots:
    if other_robot.id != myself.id and other_robot.health > 0:
      px, py = other_robot.position

      # Use barycentric coordinates to check if the point is inside the triangle
      denominator = ((left_vertex[1] - right_vertex[1]) * (tip[0] - right_vertex[0]) +
                    (right_vertex[0] - left_vertex[0]) * (tip[1] - right_vertex[1]))
      a = ((left_vertex[1] - right_vertex[1]) * (px - right_vertex[0]) +
          (right_vertex[0] - left_vertex[0]) * (py - right_vertex[1])) / denominator
      b = ((right_vertex[1] - tip[1]) * (px - right_vertex[0]) +
          (tip[0] - right_vertex[0]) * (py - right_vertex[1])) / denominator
      c = 1 - a - b

      if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1:
        distance = math.sqrt((px - tip[0]) ** 2 + (py - tip[1]) ** 2)
        if is_simple_scan:
          closest_robot_distance = min(closest_robot_distance, distance)
        else:
          detected_robots.append(Box({"id": other_robot.id, "distance": distance, "health": other_robot.health}))
  
  # Create a transparent surface, draw a scan triangle and blit it on the screen
  transparent_surface = pygame.Surface(myself.screen.get_size(), pygame.SRCALPHA)
  scan_triangle = [tip, left_vertex, right_vertex]
  pygame.draw.polygon(transparent_surface, (250, 250, 250, 5), scan_triangle)
  myself.screen.blit(transparent_surface, (0, 0))

  if is_simple_scan:
    return closest_robot_distance
  
  return detected_robots if detected_robots else None