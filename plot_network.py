import json
import os

import click
import matplotlib.pyplot as plt
from tqdm import tqdm


def int_to_color(x, colors, level):
    if type(x) is not int:
        x = x[level]
    if colors is None:
        colors = {
            '0': 'tab:blue',
            '1': 'tab:orange',
            '2': 'tab:green',
            '3': 'tab:red',
            '4': 'tab:purple',
            '5': 'tab:brown',
            '6': 'tab:pink',
            '7': 'tab:olive',
            '8': 'tab:cyan'
        }
    if str(x) in colors:
        return colors[str(x)]
    else:
        return 'tab:gray'


@click.command()
@click.argument('layout', type=click.File('r'))
@click.argument('communities', type=click.File('r'))
@click.option('--colors', type=click.File('r'), default=None)
@click.option('--level', default=0, show_default=True)
@click.argument('outfile', type=click.Path())
def main(layout, communities, colors, level, outfile):
    layout = json.load(layout)
    comm = json.load(communities)
    nodes = sorted(list(layout))
    if colors is not None:
        colors = json.load(colors)
    x = [layout[n][0] for n in nodes if n in comm]
    y = [layout[n][1] for n in nodes if n in comm]
    c = [int_to_color(comm[n], colors, level) for n in nodes if n in comm]

    plt.clf()
    fig = plt.figure()
    fig.set_size_inches(20, 20)
    plt.scatter(x, y, c=c, marker='.', s=1)
    plt.axis('off')
    plt.tight_layout()
    fig.savefig(outfile + '.pdf')
    fig.savefig(outfile + '.png')


if __name__ == '__main__':
    main()
