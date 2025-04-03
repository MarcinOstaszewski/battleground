import pygame
from helpers.scan_for_other_robots import scan_for_other_robots
from helpers.draw_robot_on_screen import draw_robot_on_screen
from helpers.calculate_new_position import calculate_new_position

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
        """Move the robot in a given direction (0-360 degrees) with 0-100 speed."""
        self.position = calculate_new_position(self, direction, speed)

    def stop(self):
        """Stop the robot."""
        self.speed = 0
    
    def scan_rich(self, angle, scan_width=5):
        """Scan specific angle and given width for other robots, displays scan triangle on the screen."""
        return scan_for_other_robots(self, angle, scan_width, pygame)

    def render(self):
        """Render the robot on the screen."""
        draw_robot_on_screen(self, pygame)
