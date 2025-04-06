import math
from constants.settings_constants import SPEED_MULTIPLIER, MAX_SPEED, ROBOT_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

def calculate_new_position(self, direction, speed):
    """Calculate the new position of the robot based on its current position, direction, and speed."""
    speed = min(speed, MAX_SPEED) * SPEED_MULTIPLIER
    robots = self.get_all_robots_from_state()
    radians = math.radians(direction)
    # Calculate change in x and y using trigonometry
    x = self.position[0] + speed * math.cos(radians)
    y = self.position[1] + speed * math.sin(radians)
    # Check for collision with screen edges, adjust position if necessary and lower health by actual speed
    if y < ROBOT_RADIUS or y > SCREEN_HEIGHT - ROBOT_RADIUS:
        y = max(ROBOT_RADIUS, min(y, SCREEN_HEIGHT - ROBOT_RADIUS))
        # Reduce health by actual speed
        self.health -= abs(self.position[1] - y) * 0.5
    if x < ROBOT_RADIUS or x > SCREEN_WIDTH - ROBOT_RADIUS:
        x = max(ROBOT_RADIUS, min(x, SCREEN_WIDTH - ROBOT_RADIUS))
        self.health -= abs(self.position[0] - x) * 0.5
    # Check for collision with other robots
    for robot in robots:
        if robot.id != self.id and robot.health > 0:
            distance = math.sqrt((x - robot.position[0]) ** 2 + (y - robot.position[1]) ** 2)
            if distance < ROBOT_RADIUS * 2:
                # if collision detected => reduce health and adjust position
                self.health -= abs(self.position[1] - y) * 0.5
                self.health -= abs(self.position[0] - x) * 0.5
                return self.position

    return (x, y)