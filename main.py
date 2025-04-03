import pygame
from helpers.get_init_state import get_init_state
from constants.screen_constants import BACKGROUND_COLOR
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

        for robot in state.robots: # Update robots
            updated_robots.append(robot.update(robot))

        state.robots = updated_robots        
        for robot in state.robots: # render robots
            robot.render(screen)

        pygame.display.flip() # Update display
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()


 