import json
import os

import click
import matplotlib.pyplot as plt
from tqdm import tqdm


def int_to_color(x, colors, level):
    if type(x) is not int:
        x = x[level]
    if colors is not None:
        with open(colors) as f:
            low = json.load(f)
    else:
        low = {
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
    if str(x) in low:
        return low[str(x)]
    else:
        return 'tab:gray'


@click.command()
@click.argument('layout')
@click.argument('communities')
@click.option('--colors', default=None)
@click.option('--level', default=0, show_default=True)
@click.argument('outfile')
def main(layout, communities, colors, level, outfile):
    with open(layout) as f:
        layout = json.load(f)
    with open(communities) as f:
        comm = json.load(f)
    nodes = sorted(list(layout))
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
