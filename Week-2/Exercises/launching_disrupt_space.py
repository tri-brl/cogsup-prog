import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name="Launching Disrupt Space")
control.initialize(exp)

# Define constants
displacement_x = 400
step_size = 10
square_length = 50
speed = 10  # milliseconds

# gap between the red square stopping point and the green square
gap = 70 


# Create squares
red_square = stimuli.Rectangle(
    (square_length, square_length), colour=(255, 0, 0),
    position=(-displacement_x, 0) 
)
green_square = stimuli.Rectangle(
    (square_length, square_length), colour=(0, 255, 0),
    position=(0, 0) 
)

# Present the squares for 1 second
red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)

# Move the red square toward the green square, but stop 70 pixels away
while red_square.position[0] + square_length + gap < green_square.position[0]:
    red_square.move((step_size, 0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(speed)

# Green square moves right after red reaches its stopping point
for x in range(displacement_x // step_size):
    green_square.move((step_size, 0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(speed)

# Show final display for 1 second
red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)

control.end()
