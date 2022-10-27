#!/usr/bin/env python
import math
import os
import re
import sys

from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(os.path.abspath('resources')),
    block_start_string='<BLOCK>',
    block_end_string='</BLOCK>',
    variable_start_string='<VAR>',
    variable_end_string='</VAR>',
    trim_blocks=True,
)


def load_tops(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    if re.match(r'^\s', lines[0]):
        raise Exception('Invalid TOP file format')

    tops = []
    top_count = 0
    for line in lines:
        if len(line) == 0 or re.match(r'^\s*#', line):
            continue
        top_count += 1
        if re.match(r'^\s', line):
            # sub top
            if 'sub' in tops[-1]:
                tops[-1]['sub'].append({'name': line})
            else:
                tops[-1]['sub'] = [{'name': line}]
        else:
            tops.append({'name': line})

    return tops, top_count


def split_tops(tops: list, total_top_count: int):
    top_split_count = math.ceil(total_top_count / 2)
    tops_left = []
    tops_left_count = 0
    previous_difference = 0
    # Split TOPs evenly
    tops_left_count += 1 + (len(tops[0]['sub']) if 'sub' in tops[0] else 0)
    while tops_left_count < top_split_count:
        top = tops.pop(0)
        tops_left.append(top)
        previous_difference = abs(tops_left_count - top_split_count)
        tops_left_count += 1 + (len(tops[0]['sub']) if 'sub' in tops[0] else 0)
    # Evaluate whether to put the middle TOP on the left or right side
    difference = abs(tops_left_count - top_split_count)
    if previous_difference >= difference:
        tops_left.append(tops.pop(0))

    return tops_left, tops


def generate_tex(values: dict):
    template = env.get_template('template.tex')

    output = template.render(**values)

    with open('main.tex', 'w') as file:
        file.write(output)
        file.flush()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python generate-tex.py <top-file>')
        exit(0)

    path = os.path.abspath(sys.argv[1])

    top_list, count = load_tops(path)
    left, right = split_tops(top_list, count)

    generate_tex({
        'tops_left': left,
        'tops_right': right,
    })
