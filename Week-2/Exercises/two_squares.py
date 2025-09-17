# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Two squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
#fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

# Create a 50px-radius square
square1 = stimuli.Rectangle((50,50), colour='blue', position=(1,12))
square2 = stimuli.Rectangle((50,50), colour='red', position=(65,12))


control.start(subject_id=1)

# Present the fixation cross on 
square1.present(clear=True, update=False)
square2.present(clear=False, update=True)

# Leave it on-screen for 500 ms
exp.clock.wait(500)