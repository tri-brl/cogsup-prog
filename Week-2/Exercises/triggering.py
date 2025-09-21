import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

exp = design.Experiment(name="Triggering")
control.initialize(exp)

# Constants
displacement_x = 400
step_size_red = 10         # red square speed
step_size_green = 30       # green square speed (3x faster)
square_length = 50
speed = 10  # ms

# Create squares at their starting positions 
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

# Move the red square right until it reaches the green square
while red_square.position[0] + square_length < green_square.position[0]:
    red_square.move((step_size_red, 0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(speed)

# Move the green square right the same distance but faster
distance_steps = displacement_x // step_size_red  # number of steps red took
for x in range(distance_steps):
    green_square.move((step_size_green, 0))  # 3x faster
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(speed)

# Show final display for 1 second
red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)

control.end()
