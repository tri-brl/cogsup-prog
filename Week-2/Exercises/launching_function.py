import expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()
exp = design.Experiment(name="Launching Function")
control.initialize(exp)

# Define constants
displacement_x = 400
step_size = 10
square_length = 50
speed = 10  

def horizontal_launching(time_gap=0, space_gap=0, green_speed_factor=1):

    # Create squares 
    red_square = stimuli.Rectangle(
        (square_length, square_length), colour=(255, 0, 0),
        position=(-displacement_x, 0)  # left of center
    )
    green_square = stimuli.Rectangle(
        (square_length, square_length), colour=(0, 255, 0),
        position=(0, 0)  # center
    )
    
    # Present initial squares
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1000)
    
    # Red square moves toward green but stops before green depending on space_gap
    stop_x = green_square.position[0] - space_gap
    while red_square.position[0] + square_length < stop_x:
        red_square.move((step_size, 0))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
        exp.clock.wait(speed)
    
    # Temporal gap before green moves
    if time_gap > 0:
        exp.clock.wait(time_gap)
    
    # Green square moves the same distance red moved, depending on speed factor
    distance = green_square.position[0] - red_square.position[0]
    green_step = step_size * green_speed_factor

    
    for x in range(displacement_x // step_size):
        green_square.move((green_step, 0))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
        exp.clock.wait(speed)
    
    # Show final positions for 1 second
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1000)

# DIsplay the 4 events

# Michottean launching (no time or space gap, same speed)
horizontal_launching()

# Launching disrupt time
horizontal_launching(time_gap=2000)

# Launching disrupt space
horizontal_launching(space_gap=70)

# Triggering
horizontal_launching(green_speed_factor=3)

control.end()
