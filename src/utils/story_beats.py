"""Function for moving to the next beat of the story"""
import random

BEATS = {
    "Set-up": "The story beginning, which establishes the backstory of the protagonists. Should introduce all "
              "important characters, the setting and the tone of the story.",
    "Catalyst": "An inciting event which changes the protagonist's trajectory, which will set them on their journey",
    "Debate": "The protagonist debates whether or not to begin the journey",
    "Break into Two": "The protagonist decides to take up call and begin the journey",
    "Fun and Games": "A break from the main plot, the fun elements of the world and characters is established",
    "Midpoint": "A return to the main plot and high stakes, the story should be at its highest or lowest point",
    "Bad Guys Close In": "Things escalate, dark forces close in on the protagonist",
    "All is Lost": "The protagonist experiences crushing defeat, raising the stakes and making a happy ending seem "
                   "impossible. The protagonist recognises defeat and loses all hope.",
    "Break into Three": "The beginning of the climax, the protagonist finds a potential solution to their situation, "
                        "but it won't be easy",
    "Finale": "The story comes to a close, the protagonist finds closure as their world changes",
}

# Initial chance to encounter a story beat
BEAT_CHANCE = 0.1  # Start at 10%
CHANCE_INC = 0.1  # Increment by 10% per choice


def change_beat(current_index: int) -> tuple:
    """Returns the next story beat and whether it is the last beat if a randomly generated number is less that the
    chance the next beat will occur. Increments the chance the next beat if the next beat has not occurred."""
    global BEATS, BEAT_CHANCE, CHANCE_INC
    if random.random() < BEAT_CHANCE:
        BEAT_CHANCE = 0.1
        if len(BEATS.keys()) == current_index + 2:
            return list(BEATS.items())[current_index + 1], True
        else:
            return list(BEATS.items())[current_index + 1], False
    else:
        BEAT_CHANCE = min(1.0, BEAT_CHANCE + CHANCE_INC)
        return None, False


def get_initial_beat() -> tuple:
    return list(BEATS.items())[0]
