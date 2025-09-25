from expyriment import design, control, stimuli, misc, io
import math

control.set_develop_mode()
exp = design.Experiment(name = "kanizsa-square",  background_colour=misc.constants.C_GREY)
control.initialize(exp)
exp.screen.clear()


length = 0.25*(exp.screen.size[0])
rad = 0.05*(exp.screen.size[1])

width,height = exp.screen.size
square = stimuli.Rectangle(size=(length,length), position=(0,0), colour=misc.constants.C_GREY)



x_positions = [(length/2),(-length/2)] #x = right screen, left screen
y_positions = [(length/2),(-length/2)] #y = top screen, bottom screen



circles = []
for x in x_positions:
    for y in y_positions:
        if y > 0:
            circle = stimuli.Circle(radius=rad, position=(x,y), colour=misc.constants.C_BLACK)
        else: 
            circle = stimuli.Circle(radius=rad, position=(x,y), colour=misc.constants.C_WHITE)
        circles.append(circle)



exp.screen.clear() #shows background colour
for crc in circles:
     crc.present(clear=False, update=False)
square.present(clear=False, update=True)


exp.keyboard.wait()

# end experiment
control.end()