# -*- coding: utf-8 -*-
import argparse
import os
from collections import namedtuple
from jinja2 import Environment, FileSystemLoader
from codecs import open
import re

Item = namedtuple('Item', ('src', 'title', 'author', 'slug'))


def render_template(template, **kwargs):
    env = Environment(loader=FileSystemLoader('.'))
    return env.get_template(template).render(**kwargs)


def slugify(string):
    return re.sub(r'[^A-Za-z]', '-', string).replace('--', '-')


def generate_output(directory, template, output, title):
    items = []
    info = os.path.join(directory, 'infos.txt')
    header_file = os.path.join(directory, 'header.html')
    with open(header_file, 'r', encoding='utf-8') as f:
        header = f.read()

    with open(info, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f):
            title_, author = line.split(' - ')
            src = "%s/%02.0f.jpg" % (directory, idx + 1)
            items.append(Item(src=src, title=title_, author=author,
                slug=slugify(title_)))

    with open(output, 'w', encoding='utf-8') as f:
        f.write(render_template(template, items=items, header=header,
                                title=title))


def main():
    parser = argparse.ArgumentParser(
            description='convert a directory to a gallery')
    parser.add_argument('directory')
    parser.add_argument('title')
    parser.add_argument('--output', default='index.html')
    parser.add_argument('--template', default='template.html')
    args = parser.parse_args()

    generate_output(args.directory, args.template, args.output,
            args.title.decode('utf-8'))

if __name__ == '__main__':
    main()
