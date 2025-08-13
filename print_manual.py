from colors import MAJOR_COLORS, MINOR_COLORS
from color_pair import color_pair_to_string

def print_color_code_manual():
    manual_lines = []
    pair_number = 1
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_str = color_pair_to_string(major_color, minor_color)
            manual_lines.append(f'{pair_number:2} | {pair_str}')
            pair_number += 1
    return '\n'.join(manual_lines)
