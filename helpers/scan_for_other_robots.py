import math
# Import moved inside the function to avoid circular import issues

def scan_for_other_robots(myself, angle, angle_range):
  angle_range = min(30, angle_range)  # Ensure a maximum angle range of 30 degrees
  robots = myself.get_all_robots_from_state()
  detected_robots = []
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
        detected_robots.append({"id": other_robot.id, "distance": distance, "health": other_robot.health})
  return detected_robots, [tip, left_vertex, right_vertex]