# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    cooking_detail = time * temperature * pressure * COOKED_CONSTANT

    if desired_state == 'well-done' and cooking_detail >= WELL_DONE: 
        return True
    if desired_state == 'medium' and cooking_detail >= MEDIUM:
        return True
    return False