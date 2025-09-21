from expyriment import design, control, stimuli, misc
import math

control.set_develop_mode()

# create experiment
exp = design.Experiment(name="Labeled shapes(with function)")
control.initialize(exp)

shape_height = 50
line_length = 50
line_width = 3
label_offset = 20 # distance between label and line


def create_labeled_polygon(n_sides, radius, colour, position, label_text):

    # create polygon vertices
    vertices = misc.geometry.vertices_regular_polygon(n_sides, radius)

    # polygon shape
    polygon = stimuli.Shape(vertex_list=vertices, colour=colour, position=position)

    # get position of top of the shape
    top_y = position[1] + radius # the shapes center point + radius length (upwards)

    # line above polygon
    line = stimuli.Rectangle(
        (line_width, line_length),
        colour="white",
        position=(position[0], top_y + line_length / 2)
    )

    # label above line
    label = stimuli.TextLine(
        label_text,
        text_size=20,
        text_colour=(255, 255, 255),
        position=(position[0], top_y + line_length + label_offset)
    )

    return polygon, line, label


# Use function to create shapes
triangle, line_triangle, label_triangle = create_labeled_polygon(
    n_sides=3,
    radius=shape_height / 2,
    colour="purple",
    position=(-85, 0),
    label_text="triangle"
)

hexagon, line_hexagon, label_hexagon = create_labeled_polygon(
    n_sides=6,
    radius=shape_height / 2,
    colour="yellow",
    position=(85, 0),
    label_text="hexagon"
)


# start experiment
control.start(subject_id=1)

# display shapes
triangle.present(clear=True, update=False)
hexagon.present(clear=False, update=False)
line_triangle.present(clear=False, update=False)
line_hexagon.present(clear=False, update=False)
label_triangle.present(clear=False, update=False)
label_hexagon.present(clear=False, update=True)

# wait for a key press
exp.clock.wait(2000)

# end experiment
control.end()
