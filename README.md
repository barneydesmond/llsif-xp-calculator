# llsif-xp-calculator

A simple command-line calculator written in Python, to tell you how far your idol is from hitting her Experience ceiling in the popular mobile game *Love Live: School Idol Festival*.

## Usage

    exp.py [-h] [-r {N,R,SR,UR}] [-u] current_level [partial]

Simply call the script, passing in:

1. Rarity (defaults to Normal if not given)
2. Unawakened/Awakened status (assumes Awakened unless specified)
3. Current level
4. Any XP progress towards the next level (optional, we assume zero progress otherwise)

## Example usage

1. Normal idol, just scouted at level 9-and-a-bit, how far to unawakened (level 30) XP ceiling?

        $ python exp.py -u 9 46
        You are at level 9/30, you have spent 404, and have 4071 more exp to go

2. Normal idol, freshly awakened, was already sitting at XP ceiling

        $ python exp.py 30
        You are at level 30/40, you have spent 4475, and have 3525 more exp to go

3. Typical SR idol, ceiling is at level 60, partially levelled

        $ python exp.py -r SR -u 26 142
        You are at level 26/60, you have spent 6750, and have 17053 more exp to go

4. Awakened UR idol, partially levelled

        $ python exp.py -r UR 86 712
        You are at level 86/100, you have spent 66061, and have 13639 more exp to go
