import pygame
import math
from helpers.scan_for_other_robots import scan_for_other_robots
from helpers.draw_robot_on_screen import draw_robot_on_screen

class Robot:
    def __init__(self, robot, screen):
        self.screen = screen
        self.id = robot["id"]
        self.update = robot["update"]
        self.get_all_robots_from_state = robot["get_all_robots_from_state"]
        self.position = robot["position"]
        self.speed = 0
        self.max_speed = 5 # Default max speed if not specified
        self.health = 100
        self.direction = robot["direction"]
        self.aim_angle = robot["aim_angle"]
        self.vars = robot["vars"]
        # self.equipped_with = robot["equipped_with"]

    def move(self, direction, speed):
        """Move the robot in a given direction (degrees) and speed."""
        radians = math.radians(direction)
        # Calculate change in x and y using trigonometry
        x = self.position[0] + speed * math.cos(radians)
        y = self.position[1] + speed * math.sin(radians)
        # Ensure the robot stays within the screen bounds
        x = max(0, min(x, self.screen.get_width()))
        y = max(0, min(y, self.screen.get_height()))
        self.position = (x, y)
    
    def scan(self, angle, scan_width=5):
        """Scan specific angle and given width for other robots, displays scan triangle on the screen."""
        scan_result, scan_triangle = scan_for_other_robots(self, angle, scan_width)
        # Draw the scan triangle for visualization
        pygame.draw.polygon(self.screen,  (60, 60, 60, 10), scan_triangle)
        return scan_result

    def render(self, screen):
        """Render the robot on the screen."""
        draw_robot_on_screen(self, pygame, screen)
