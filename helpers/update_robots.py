def update_robots(state):
  for robot in state.robots:
    if robot.health <= 0:
      robot.speed = 0
      state.updated_robots.append(robot)
    else:
      state.updated_robots.append(robot.update(robot))

  for robot in state.robots:
    robot.render()
