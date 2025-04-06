import pygame
from helpers import scan_for_other_robots, draw_robot_on_screen, calculate_new_position
from constants.settings_constants import MAX_SHOT_RANGE
class Robot:
    def __init__(self, robot, screen):
        self.screen = screen
        self.id = robot["id"]
        self.update = robot["update"] # function from specific robot's file in Instructions folder
        self.get_all_robots_from_state = robot["get_all_robots_from_state"]
        self.append_bullet = robot["append_bullet"]
        self.position = robot["position"]
        self.speed = 0
        self.max_speed = 5 # Default max speed if not specified
        self.health = 100
        self.direction = robot["direction"]
        self.aim_angle = robot["aim_angle"]
        self.vars = robot["vars"]
        self.bullet_shot_counter = 0
        # self.equipped_with = robot["equipped_with"]

    def move(self, direction, speed):
        """Move the robot in a given direction (0-360 degrees) with 0-100 speed."""
        self.position = calculate_new_position(self, direction, speed)

    def stop(self):
        """Stop the robot."""
        self.speed = 0
    
    def scan_rich(self, angle, scan_width=5):
        """Scan specific angle in given width for all other robots."""
        return scan_for_other_robots(self, angle, scan_width, pygame, is_simple_scan=False)
    
    def scan(self, angle, scan_width=5):
        """Scan specific angle in given width for distance to the closest robot."""
        return scan_for_other_robots(self, angle, scan_width, pygame, is_simple_scan=True)
        
    def getX(self):
        return self.position[0]

    def getY(self):
        return self.position[1]
    
    def get_screen_width(self):
        return self.screen.get_width()
    
    def get_screen_height(self):
        return self.screen.get_height()
    
    def shoot(self, shoot_angle, range):
        """Shoot a bullet in a given direction for a given range."""
        if self.bullet_shot_counter == 0:
            self.bullet_shot_counter = 100
            self.append_bullet({
                "position": self.position,
                "direction": shoot_angle,
                "x_shift": 0,
                "y_shift": 0,
                "range_covered": 0,
                "range": int(min(MAX_SHOT_RANGE, range))
            })

    def render(self):
        """Render the robot on the screen."""
        self.bullet_shot_counter -= 1 if self.bullet_shot_counter > 0 else 0
        draw_robot_on_screen(self, pygame)
