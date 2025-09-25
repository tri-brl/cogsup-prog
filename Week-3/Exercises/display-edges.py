from expyriment import design, control, stimuli, misc
import math

control.set_develop_mode()
exp = design.Experiment(name = "edges")
control.initialize(exp)

length = 0.05*(exp.screen.size[0])

width,height = exp.screen.size

x_positions = [((-width//2) + (length/2)), ((width//2) - (length/2))] #x = laft screen, right screen
y_positions = [((-height//2) + (length/2)), ((height//2) - (length/2))] #y = bottom screen, top screen

squares = []
for x in x_positions:
    for y in y_positions:
        square = stimuli.Rectangle(size=(length, length),
                                   position=(x, y),
                                   colour=(255, 0, 0),
                                   line_width=5)
        squares.append(square)

for sq in squares[:-1]: #until second last square, finally update all of them
     sq.present(clear=False, update=False)
squares[-1].present(clear=False, update=True)

exp.keyboard.wait()

control.end()