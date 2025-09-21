# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()
exp = design.Experiment(name = "Two squares")
control.initialize(exp)

# Create 2 50px-radius squares 200 pixels apart
square1 = stimuli.Rectangle((50,50), colour='red', position=(-100,0))
square2 = stimuli.Rectangle((50,50), colour='green', position=(100,0))


control.start(subject_id=1)

# Present the two squares
square1.present(clear=True, update=False)
square2.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()
control.end()