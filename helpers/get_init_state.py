import os, math, random
from Robot import Robot

INSTRUCTIONS_FOLDER = "Instructions"

class GameState:
    """Class to represent the initial state of the game."""
    def __init__(self):
        self.robots = []
        self.get_all_robots_from_state = self.get_all_robots_from_state
        self.resources = {
            "iron": [],
        }
        self.bullets = []
        self.updated_robots = []

    def get_all_robots_from_state(self):
        return self.robots
    
    def reset_updated_bullets(self):
        self.updated_robots = []
    
    def append_bullet(self, bullet):
        """Append a bullet to the state."""
        self.bullets.append(bullet)
    
    def get_all_bullets_from_state(self):
        return self.bullets

def load_robot_instructions():
    robot_files = [os.path.splitext(f)[0] for f in os.listdir(INSTRUCTIONS_FOLDER) if f.endswith(".py")]
    return robot_files

def get_init_robot_pos_and_direction(robot_index, number_of_all_robots, SCREEN_WIDTH, SCREEN_HEIGHT):
    """Get the position of a robot based on its index and the total number of robots."""
    angle = 360 / number_of_all_robots
    x = int(SCREEN_WIDTH / 2 + SCREEN_WIDTH / 3 * math.cos(math.radians(angle * robot_index)))
    y = int(SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 3 * math.sin(math.radians(angle * robot_index)))
    return (x, y), angle * robot_index - 180

def get_init_state(screen):
    """Create the initial state of the game."""
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    state = GameState()
    robot_instructions = load_robot_instructions()
    for i, instruction in enumerate(robot_instructions):
        position, direction = get_init_robot_pos_and_direction(i, len(robot_instructions), SCREEN_WIDTH, SCREEN_HEIGHT)
        robot_module = __import__(f"{INSTRUCTIONS_FOLDER}.{instruction}")
        instructions = getattr(robot_module, instruction)
        robot_vars = instructions.set_vars() if hasattr(instructions, 'set_vars') else {}
        update_function = instructions.update if hasattr(instructions, 'update') else None

        robot_init_data = {
            "id": i,
            "update": update_function,
            "get_all_robots_from_state": state.get_all_robots_from_state,
            "append_bullet": state.append_bullet,
            "position": position,
            "direction": direction,
            "aim_angle": random.uniform(0, 360),
            "vars": robot_vars,
            "color": robot_vars.get("color", (0, 0, 0)),
            # "equipped_with": [],
            # "get_all_bullets_from_state": state.get_all_bullets_from_state,
        }
        state.robots.append(Robot(robot_init_data, screen))
    return state