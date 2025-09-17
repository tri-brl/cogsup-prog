# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()
# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# Create a fixation cross (color, size, and position will take on default values)
fixation = stimuli.FixCross() # At this stage the fixation cross is not yet rendered

# Create a 50px-radius square
square = stimuli.Rectangle((50,50), colour='blue')

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross on 
square.present(clear=True, update=False)
fixation.present(clear=False, update=True)

# Leave it on-screen for 500 ms
exp.clock.wait(500)

# Remove the cross and replace it with a square
square.present(clear=True, update=True)
#exp.clock.wait(500)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()