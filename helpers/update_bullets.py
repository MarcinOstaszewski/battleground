import math
from constants.settings_constants import BULLET_SPEED, ROBOT_RADIUS

def update_bullets(state, screen, pygame):
    state.reset_updated_bullets() # Reset updated bullets list
    for bullet in state.bullets: # Update bullets
        if bullet["x_shift"] == 0 and bullet["y_shift"] == 0: # First frame of the bullet - set x and y shift
            bullet["x_shift"] = BULLET_SPEED * math.cos(math.radians(bullet["direction"]))
            bullet["y_shift"] = BULLET_SPEED * math.sin(math.radians(bullet["direction"]))
        bullet["range_covered"] += BULLET_SPEED
        bullet["position"] = (bullet["position"][0] + bullet["x_shift"], bullet["position"][1] + bullet["y_shift"])
        pygame.draw.circle(screen, (20, 20, 20), bullet["position"], 5)
        if bullet["range_covered"] >= bullet["range"]:
            for robot in state.robots:
                distance = math.sqrt((robot.position[0] - bullet["position"][0])**2 + (robot.position[1] - bullet["position"][1])**2)
                if distance <= ROBOT_RADIUS * 1.5:
                    robot.health -= (ROBOT_RADIUS * 1.5 - distance)
            state.bullets.remove(bullet)
