import pygame
import math
from helpers.get_init_state import get_init_state
from constants.screen_constants import BACKGROUND_COLOR
from constants.settings_constants import BULLET_SPEED
from helpers.check_for_quit_events import check_for_quit_events

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
print(f"Screen size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Battleground")

# Main loop
def main():
    clock = pygame.time.Clock()
    state = get_init_state(SCREEN_WIDTH, SCREEN_HEIGHT, screen)

    running = True
    while running:
        running = check_for_quit_events(pygame, running)

        screen.fill(BACKGROUND_COLOR) # Draw battleground

        updated_robots = [] # Create new state for the next frame

        for bullet in state.bullets: # Update bullets
            if bullet["x_shift"] == 0 and bullet["y_shift"] == 0:
                bullet["x_shift"] = BULLET_SPEED * math.cos(math.radians(bullet["direction"]))
                bullet["y_shift"] = BULLET_SPEED * math.sin(math.radians(bullet["direction"]))
            bullet["range_covered"] += BULLET_SPEED
            bullet["position"] = (bullet["position"][0] + bullet["x_shift"], bullet["position"][1] + bullet["y_shift"])
            pygame.draw.circle(screen, (20, 20, 20), bullet["position"], 5)
            if bullet["range_covered"] >= bullet["range"]:
                state.bullets.remove(bullet)

        for robot in state.robots: # Update robots
            if robot.health <= 0:
                robot.speed = 0
                updated_robots.append(robot)
            else:
                updated_robots.append(robot.update(robot))

        state.robots = updated_robots        
        for robot in state.robots: # render robots
            robot.render()

        pygame.display.flip() # Update display
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()


 