from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

fixation.present(clear=True, update=True) 
exp.clock.wait(500)

#added this line which clears the back buffer 'Ready' & updates it to have the cross, which is displayed later along w the square:
fixation.present(clear=True, update=False) 
square.present(clear=False, update=True)
exp.keyboard.wait()

control.end()