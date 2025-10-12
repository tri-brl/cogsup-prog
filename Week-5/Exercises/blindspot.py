
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_1, K_2, K_SPACE
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)
key_map = {
    K_UP: "UP",
    K_DOWN: "DOWN",
    K_LEFT: "LEFT",
    K_RIGHT: "RIGHT",
    K_1: "1",
    K_2: "2",
    K_SPACE: "SPACE"
}
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c
instructions = (
        "Close your left eye and focus your right eye on the cross.\n"
        "Keep looking at the cross and slowly move toward the screen.\n"
        "At a certain distance (depending on your screen size), the black circle will disappear — this is your blind spot.\n"
        "Move slightly closer or farther and the circle will reappear.\n\n"
        "Repeat with your other eye: cover your right eye, look at the circle with your left eye, and move closer until the cross disappears.\n\n"
        "Use the arrow keys to modify the circle position and size:\n"
        "-Use the arrow keys to move the circle up, down, left, or right.\n"
        "-Press 1 to make the circle smaller.\n"
        "-Press 2 to make the circle larger.\n"
        "-Press Spacebar to end the experiment.")

def run_trial(eye):
    control.start(subject_id=1)
    text = stimuli.TextScreen(text=instructions, heading="Test your blindspot!")
    text.present(clear = True, update= True)
    exp.keyboard.wait()
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=([300, 0]if eye=='right' else [-300,0]))
    fixation.preload()
    radius = 75
    circle = make_circle(radius)
    fixation.present(clear=True, update=False)
    circle.present(clear=False, update=True)
    # Movement loop
    running = True
    offset = 20
    while running:
        key = exp.keyboard.check() 
        if key == K_RIGHT:
            circle.move((offset, 0))
        elif key == K_LEFT:
            circle.move((-offset, 0))
        elif key == K_UP:
            circle.move((0, offset))
        elif key == K_DOWN:
            circle.move((0, -offset))
        elif key == K_1:  # shrink
            radius = max(5, radius - 5)  
            pos = circle.position 
            circle = make_circle(radius, pos=pos)
        elif key == K_2:  # grow
            radius += 5
            pos = circle.position
            circle = make_circle(radius, pos=pos)
        elif key == K_SPACE:
            break
        fixation.present(clear=True, update=False)
        circle.present(clear=False, update=True)
        if key is not None:
            exp.data.add([eye, key_map.get(key, str(key)), radius, circle.position[0], circle.position[1]])
    control.end()
run_trial('left')
    
