import math
from constants.screen_constants import ROBOT_RADIUS

def draw_robot_on_screen(self, pygame, screen):
  pygame.draw.circle(screen, self.vars.color, self.position, ROBOT_RADIUS)
  # Calculate the points of the front triangle
  base_left_x = self.position[0] + ROBOT_RADIUS * 0.6 * math.cos(math.radians(self.direction + 120))
  base_left_y = self.position[1] + ROBOT_RADIUS * 0.6 * math.sin(math.radians(self.direction + 120))
  base_right_x = self.position[0] + ROBOT_RADIUS * 0.6 * math.cos(math.radians(self.direction - 120))
  base_right_y = self.position[1] + ROBOT_RADIUS * 0.6 * math.sin(math.radians(self.direction - 120))
  tip_x = self.position[0] + ROBOT_RADIUS * math.cos(math.radians(self.direction))
  tip_y = self.position[1] + ROBOT_RADIUS * math.sin(math.radians(self.direction))
  # Draw the triangle
  darker_tone = tuple(max(0, c - 80) for c in self.vars.color)  # Calculate a darker tone of self.vars.color
  pygame.draw.polygon(screen, darker_tone, [(base_left_x, base_left_y), (base_right_x, base_right_y), (tip_x, tip_y)])
  # # # Draw the robot's aim angle
  # aim_x = self.position[0] + ROBOT_RADIUS * 0.9 * math.cos(math.radians(self.aim_angle))
  # aim_y = self.position[1] + ROBOT_RADIUS * 0.9 * math.sin(math.radians(self.aim_angle))
  # pygame.draw.line(screen, (10, 10, 10), self.position, (aim_x, aim_y), 4)