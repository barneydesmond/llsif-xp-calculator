# llsif-xp-calculator

A simple calculator to tell you how far your idol is from hitting her Experience ceiling

## Usage

    exp.py [-h] [-r {N,R,SR,UR}] [-u] current_level [partial]

Simply call the script, passing in:

1. Rarity (defaults to Normal if not given)
2. Unawakened/Awakened status (assumes Awakened unless specified)
3. Current level
4. Any XP progress towards the next level (optional, we assume zero progress otherwise)

## Example usage

1. Normal idol, just scouted at level 9-and-a-bit, how far to unawakened (level 30) XP ceiling?

        python exp.py -u 9 46

2. Normal idol, freshly awakened, was already sitting at XP ceiling

        python exp.py 30

3. Typical SR idol, ceiling is at level 60, partially levelled

        python exp.py -r SR -u 26 142

4. Awakened UR idol, partially levelled

        python exp.py -r UR 86 712
