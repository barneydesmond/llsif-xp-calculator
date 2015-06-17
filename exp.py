import argparse

AWAKE,ASLEEP = True,False 

NORMAL_LEVELS = { 
	2: 6, 3: 18, 4: 28, 5: 40, 6: 51, 7: 61, 8: 72, 9: 82, 10: 93,
	11: 104, 12: 114, 13: 124, 14: 135, 15: 145, 16: 156, 17: 165, 18: 176, 19: 187, 20: 196,
	21: 207, 22: 217, 23: 226, 24: 238, 25: 247, 26: 257, 27: 268, 28: 277, 29: 288, 30: 297,
	31: 308, 32: 317, 33: 328, 34: 337, 35: 348, 36: 358, 37: 367, 38: 377, 39: 388, 40: 397
}

RARE_LEVELS = {
	2: 14, 3: 31, 4: 45, 5: 55, 6: 67, 7: 76, 8: 85, 9: 94, 10: 103,
	11: 110, 12: 119, 13: 125, 14: 134, 15: 140, 16: 148, 17: 155, 18: 161, 19: 168, 20: 174,
	21: 181, 22: 187, 23: 193, 24: 199, 25: 206, 26: 211, 27: 217, 28: 223, 29: 228, 30: 235,
	31: 240, 32: 245, 33: 251, 34: 256, 35: 262, 36: 267, 37: 272, 38: 277, 39: 283, 40: 288,
	41: 292, 42: 298, 43: 303, 44: 308, 45: 313, 46: 317, 47: 323, 48: 327, 49: 332, 50: 337,
	51: 342, 52: 346, 53: 351, 54: 356, 55: 360, 56: 365, 57: 370, 58: 374, 59: 378, 60: 383
}

SUPERRARE_LEVELS = {
	2: 54, 3: 98, 4: 127, 5: 150, 6: 169, 7: 187, 8: 203, 9: 218, 10: 232,
	11: 245, 12: 257, 13: 269, 14: 281, 15: 291, 16: 302, 17: 311, 18: 322, 19: 331, 20: 340,
	21: 349, 22: 358, 23: 366, 24: 374, 25: 383, 26: 391, 27: 398, 28: 406, 29: 413, 30: 421,
	31: 428, 32: 435, 33: 442, 34: 449, 35: 456, 36: 462, 37: 469, 38: 475, 39: 482, 40: 488,
	41: 494, 42: 500, 43: 507, 44: 512, 45: 518, 46: 524, 47: 530, 48: 536, 49: 541, 50: 547,
	51: 552, 52: 558, 53: 563, 54: 568, 55: 574, 56: 579, 57: 584, 58: 590, 59: 594, 60: 600,
	61: 605, 62: 609, 63: 615, 64: 619, 65: 625, 66: 629, 67: 634, 68: 639, 69: 643, 70: 648,
	71: 653, 72: 657, 73: 662, 74: 667, 75: 670, 76: 676, 77: 680, 78: 684, 79: 689, 80: 693
}

ULTRARARE_LEVELS = {
	2: 201, 3: 294, 4: 345, 5: 382, 6: 411, 7: 438, 8: 460, 9: 481, 10: 499,
	11: 517, 12: 532, 13: 547, 14: 561, 15: 574, 16: 587, 17: 598, 18: 611, 19: 621, 20: 631,
	21: 642, 22: 651, 23: 661, 24: 670, 25: 679, 26: 687, 27: 696, 28: 704, 29: 712, 30: 720,
    31: 727, 32: 734, 33: 742, 34: 749, 35: 755, 36: 763, 37: 769, 38: 775, 39: 782, 40: 788,
    41: 794, 42: 800, 43: 806, 44: 812, 45: 818, 46: 823, 47: 829, 48: 834, 49: 840, 50: 845,
    51: 850, 52: 856, 53: 860, 54: 866, 55: 870, 56: 875, 57: 880, 58: 885, 59: 890, 60: 894,
    61: 899, 62: 903, 63: 908, 64: 912, 65: 917, 66: 921, 67: 925, 68: 930, 69: 933, 70: 938,
    71: 942, 72: 946, 73: 950, 74: 954, 75: 959, 76: 961, 77: 966, 78: 970, 79: 974, 80: 977,
    81: 981, 82: 985, 83: 988, 84: 992, 85: 996, 86: 999, 87: 1003, 88: 1006, 89: 1010, 90: 1013,
    91: 1017, 92: 1020, 93: 1024, 94: 1027, 95: 1030, 96: 1034, 97: 1037, 98: 1040, 99: 1043, 100: 1047
}

TABLES = { "N":NORMAL_LEVELS, "R":RARE_LEVELS, "SR":SUPERRARE_LEVELS, "UR":ULTRARARE_LEVELS }
LEVEL_CAPS = {
    "N":  { ASLEEP: 30, AWAKE: 40 },
    "R":  { ASLEEP: 40, AWAKE: 60 },
    "SR": { ASLEEP: 60, AWAKE: 80 },
    "UR": { ASLEEP: 80, AWAKE: 100 }
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate required EXP for LLSIF card levelling")
    parser.add_argument("-r", "--rarity", dest="rarity", default="N", choices=["N", "R", "SR", "UR"], help="Specify card rarity")
    parser.add_argument("-u", "--unawakened", dest="awake", action='store_false', help="Limit the EXP calculation to the lower level cap")
    parser.add_argument("current_level", nargs=1, type=int, help="The current level of the card you're training")
    parser.add_argument("partial", nargs='?', default=0, const=0, type=int, help="The number of exp you have towards the next level")
    args = parser.parse_args()
    print args

    table = TABLES[args.rarity]
    current_level = args.current_level[0]
    partial_spend = args.partial
    rarity = args.rarity
    awake = args.awake
    level_cap = LEVEL_CAPS[rarity][awake]

    amount_spent = sum([ x[1] for x in table.items() if x[0] <= current_level ]) + partial_spend
    required_exp = sum([ x[1] for x in table.items() if x[0] > current_level and x[0] <= level_cap ]) - partial_spend

    print("You are at level {}/{}, you have spent {}, and have {} more exp to go".format(current_level, level_cap, amount_spent, required_exp))
