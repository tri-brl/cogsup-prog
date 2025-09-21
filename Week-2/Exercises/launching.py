import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name="Launching")
control.initialize(exp)

# Define constants
displacement_x = 400
step_size = 10
square_length = 50
speed = 10  # in ms

# Create squares at their starting positions
red_square = stimuli.Rectangle(
    (square_length, square_length), colour=(255, 0, 0),
    position=(-displacement_x, 0)  # 400pixels from the center
)
green_square = stimuli.Rectangle(
    (square_length, square_length), colour=(0, 255, 0),
    position=(0, 0)  # center
)

# Present the squares for 1 second
red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)

# Move the red square right until it reaches the green square
while red_square.position[0] + square_length < green_square.position[0]: # While red's right edge is still left of green
    red_square.move((step_size, 0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(speed)

# Move the green square right the same distance
for x in range(displacement_x // step_size): # Calculates how many steps need to be taken to reach the the displacement amount
    green_square.move((step_size, 0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(speed)

# Show final display for 1 second
red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)

control.end()
