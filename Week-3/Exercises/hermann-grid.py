from expyriment import design, control, stimuli, misc

control.set_develop_mode()


def herm_grid(size, clr, space, n_rows, n_cols, bg):
    exp = design.Experiment(name="hermann-grid", background_colour=bg)
    control.initialize(exp)

    # Total grid size
    total_width = n_cols * size + (n_cols - 1) * space #total width of each square + space between each columns
    total_height = n_rows * size + (n_rows - 1) * space #total height of each square + space between each columns

    squares = []
    for i in range(n_rows):
        for j in range(n_cols):
            x = j * (size + space) - total_width/2 + size/2 # moves the squares to the left based on how many there are, centers them
            y = i * (size + space) - total_height/2 + size/2 # moves the squares down based on how many there are, centers them
            square = stimuli.Rectangle(size=(size, size), position=(x, y), colour=clr)
            squares.append(square)

    exp.screen.clear()
    for sq in squares:
        sq.present(clear=False, update=False)
    exp.screen.update()

    exp.keyboard.wait()
    control.end()


# Example usage
herm_grid(size=50, clr=(0,0,0), space=10, n_rows=6, n_cols=6, bg=(200,200,200))

