"""Function for moving to the next beat of the story"""
import random

BEATS = {
    "Set-up": "the beginning of the story, establishes the backstory of the protagonists, introduces all "
              "important characters, the setting and the tone of the story",
    "Catalyst": "an inciting event which changes the protagonist's trajectory, setting them on their journey",
    "Debate": "the protagonist debates whether or not to begin the journey",
    "Break into Two": "the protagonist decides to take up call and begin the journey",
    "Fun and Games": "a break from the main plot, the fun elements of the world and characters is established",
    "Midpoint": "a return to the main plot and high stakes, the story should be at its highest or lowest point",
    "Bad Guys Close In": "things escalate, dark forces close in on the protagonist",
    "All is Lost": "the protagonist experiences and recognises a crushing defeat, losing all hope, raising the stakes "
                   "and making a happy ending seem impossible",
    "Break into Three": "the beginning of the climax, the protagonist finds a potential solution to their situation, "
                        "but it won't be easy",
    "Finale": "the story comes to a close in a final scene, the protagonist finds closure as their world changes and "
              "all plot points are wrapped up and completed",
}

# Initial chance to encounter a story beat
BEAT_CHANCE = 0.1  # Start at 10%
CHANCE_INC = 0.1  # Increment by 10% per choice


def change_beat(current_index: int) -> tuple:
    """Returns the next story beat index and whether it is the last beat if a randomly generated number is less that the
    chance the next beat will occur. Increments the chance the next beat if the next beat has not occurred."""
    global BEATS, BEAT_CHANCE, CHANCE_INC
    if random.random() < BEAT_CHANCE:
        BEAT_CHANCE = 0.1
        if len(BEATS.keys()) == current_index + 2:
            return current_index + 1, True
        else:
            return current_index + 1, False
    else:
        BEAT_CHANCE = min(1.0, BEAT_CHANCE + CHANCE_INC)
        return None, False
