from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f
import random

""" Constants """
KEYS = [K_j, K_f]
TRIAL_TYPES = ['match', 'mismatch']
COLORS = ['red', 'blue', 'green', 'orange']
N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16
subject_id = 1

INSTR_START = """
In this task, you have to indicate whether the meaning of a word and the color of its font match.
Press J if they do, F if they don't.\n
Press SPACE to continue.
"""
INSTR_MID = """You have finished half of the experiment, well done!
Take a break then press SPACE to move on to the second half."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = "YOU ARE RIGHT, HOORAY!"
FEEDBACK_INCORRECT = "OOPS, THAT'S NOT RIGHT :("

""" Helper functions """
def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

def present_for(*stims, t=1000):
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    exp.clock.wait(t)

""" Initialize experiment """
exp = design.Experiment(name="Balanced Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block', 'trial', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
for w in COLORS:
    for c in COLORS:
        stims[w][c].preload()

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
feedback_correct.preload()
feedback_incorrect.preload()

""" Balanced trial creation """
match_trials = [{'trial_type': 'match', 'word': c, 'color': c} for c in COLORS]
mismatch_trials = [{'trial_type': 'mismatch', 'word': w, 'color': c}
                   for w in COLORS for c in COLORS if w != c]
random.shuffle(mismatch_trials)
mismatch_trials = mismatch_trials[:len(match_trials)]

base_trials = match_trials + mismatch_trials
random.shuffle(base_trials)

# split into 8 blocks of 16 trials (8 match, 8 mismatch)
blocks = [base_trials[:N_TRIALS_IN_BLOCK], base_trials[N_TRIALS_IN_BLOCK:]]

""" Trial execution """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)
    correct = (key == K_j) if trial_type == "match" else (key == K_f)
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1500) 
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])

""" Run experiment """
control.start(subject_id=subject_id)
present_instructions(INSTR_START)

for block_id, block in enumerate(blocks, 1):
    for trial_id, trial in enumerate(block, 1):
        run_trial(block_id, trial_id, trial["trial_type"], trial["word"], trial["color"])
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)

present_instructions(INSTR_END)
control.end()
