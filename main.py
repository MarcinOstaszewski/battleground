import pygame
from helpers import update_bullets, get_init_state, update_robots, check_for_quit_events
from constants.settings_constants import BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
# SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    clock = pygame.time.Clock()
    state = get_init_state(screen)

    running = True
    while running:
        running = check_for_quit_events(pygame, running)

        screen.fill(BACKGROUND_COLOR) # Draw battleground

        update_bullets(state, screen, pygame)

        update_robots(state)

        pygame.display.flip() # Update display
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
