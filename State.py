# class State:
#     def __init__(self):
#         self.robots = {}

#     def initialize_robots(self, robots):
#         """Initialize the state with robot properties."""
#         for robot in robots:
#             self.robots[robot.id] = {
#                 "position": robot.position,
#                 "speed": robot.speed,
#                 "direction": robot.direction,
#             }

#     def update_robot(self, robot_id, position, speed, direction):
#         """Update the state for a specific robot."""
#         self.robots[robot_id] = {
#             "position": position,
#             "speed": speed,
#             "direction": direction,
#         }

#     def get_robot_state(self, robot_id):
#         """Retrieve the state for a specific robot."""
#         return self.robots.get(robot_id, None)