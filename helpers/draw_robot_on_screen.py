import math
from constants.screen_constants import ROBOT_RADIUS

def draw_robot_on_screen(self, pygame):
  pygame.draw.circle(self.screen, self.vars.color, self.position, ROBOT_RADIUS)
  # Calculate the points of the front triangle
  base_left_x = self.position[0] + ROBOT_RADIUS * 0.4 * math.cos(math.radians(self.direction + 130))
  base_left_y = self.position[1] + ROBOT_RADIUS * 0.4 * math.sin(math.radians(self.direction + 130))
  base_right_x = self.position[0] + ROBOT_RADIUS * 0.4 * math.cos(math.radians(self.direction - 130))
  base_right_y = self.position[1] + ROBOT_RADIUS * 0.4 * math.sin(math.radians(self.direction - 130))
  tip_x = self.position[0] + ROBOT_RADIUS * math.cos(math.radians(self.direction))
  tip_y = self.position[1] + ROBOT_RADIUS * math.sin(math.radians(self.direction))
  # Draw the triangle
  darker_tone = tuple(max(0, c - 80) for c in self.vars.color)  # Calculate a darker tone of self.vars.color
  pygame.draw.polygon(self.screen, darker_tone, [(base_left_x, base_left_y), (base_right_x, base_right_y), (tip_x, tip_y)])
  # Draw the robot's health bar
  health_bar_width = ROBOT_RADIUS * 2
  health_bar_height = 5
  health_bar_x = self.position[0] - health_bar_width / 2
  health_bar_y = self.position[1] - ROBOT_RADIUS - 10
  health_percentage = self.health / 100
  health_bar_color = (255, 0, 0) if self.health < 50 else (0, 255, 0)
  pygame.draw.rect(self.screen, (0, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
  pygame.draw.rect(self.screen, health_bar_color, (health_bar_x, health_bar_y, health_bar_width * health_percentage, health_bar_height))
  # # # Draw the robot's aim angle
  # aim_x = self.position[0] + ROBOT_RADIUS * 0.9 * math.cos(math.radians(self.aim_angle))
  # aim_y = self.position[1] + ROBOT_RADIUS * 0.9 * math.sin(math.radians(self.aim_angle))
  # pygame.draw.line(screen, (10, 10, 10), self.position, (aim_x, aim_y), 4)