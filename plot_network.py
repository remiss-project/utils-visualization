import json
import os

import click
import matplotlib.pyplot as plt
from tqdm import tqdm


def get_default_colors():
    directory = os.path.dirname(__file__)
    return os.path.join(directory, 'default_community_colors.json')


def int_to_color(x, colors):
    if str(x) in colors:
        return colors[str(x)]
    else:
        return 'tab:gray'


@click.command()
@click.argument('layout', type=click.File('r'))
@click.argument('communities', type=click.File('r'))
@click.option('--colors', type=click.File('r'), default=get_default_colors())
@click.argument('outfile', type=click.Path())
def main(layout, communities, colors, outfile):
    layout = json.load(layout)
    comm = json.load(communities)
    colors = json.load(colors)
    nodes = sorted(list(layout))
    x = [layout[n][0] for n in nodes if n in comm]
    y = [layout[n][1] for n in nodes if n in comm]
    c = [int_to_color(comm[n], colors) for n in nodes if n in comm]

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
