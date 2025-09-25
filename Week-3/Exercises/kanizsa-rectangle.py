from expyriment import design, control, stimuli, misc

control.set_develop_mode()

# Initialize experiment with grey background
exp = design.Experiment(name="kanizsa-rectangle", background_colour=misc.constants.C_GREY)
control.initialize(exp)


def kan_rectangle(ratio, rect_scale, circle_scale):
    scr_width, scr_height = exp.screen.size

    # Rectangle size
    length = rect_scale * scr_height
    width = rect_scale * scr_width
    rect_width = ratio[0] * width
    rect_height = ratio[1] * length

    Rectangle = stimuli.Rectangle(size=(rect_width, rect_height),
                                  position=(0, 0),
                                  colour=misc.constants.C_GREY)

    # Circles at rectangle corners
    x_positions = [(rect_width/2), (-rect_width/2)]
    y_positions = [(rect_height/2), (-rect_height/2)]

    rad = circle_scale * scr_height

    circles = []
    for x in x_positions:
        for y in y_positions:
            if y > 0:
                circle = stimuli.Circle(radius=rad, position=(x,y), colour=misc.constants.C_BLACK)
            else: 
                circle = stimuli.Circle(radius=rad, position=(x,y), colour=misc.constants.C_WHITE)
            circles.append(circle)

    # Display all objects on screen
    exp.screen.clear()
    for crc in circles:
        crc.present(clear=False, update=False)
    Rectangle.present(clear=False, update=True)


# Example
kan_rectangle(ratio=(1.5, 1), rect_scale=0.25, circle_scale=0.05)

exp.keyboard.wait()
control.end()
