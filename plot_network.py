import json
import os

import click
import matplotlib.pyplot as plt
from tqdm import tqdm


def get_default_colors():
    directory = os.path.dirname(__file__)
    return os.path.join(directory, 'default_community_colors.json')


def plot_network(layout, comm, colors, size, outfile):
    nodes = sorted(list(layout))
    x = [layout[n][0] for n in nodes if n in comm]
    y = [layout[n][1] for n in nodes if n in comm]
    c = [
        colors[str(comm[n])] if str(comm[n]) in colors else 'tab:gray'
        for n in nodes if n in comm
    ]

    plt.clf()
    fig = plt.figure()
    fig.set_size_inches(size, size)
    plt.scatter(x, y, c=c, marker='.', s=1)
    plt.axis('off')
    plt.tight_layout()
    fig.savefig(outfile + '.pdf')
    fig.savefig(outfile + '.png')
    plt.close()


@click.command()
@click.argument('layout', type=click.File('r'))
@click.argument('communities', type=click.File('r'))
@click.option('--colors', type=click.File('r'), default=get_default_colors())
@click.option('--size', type=click.IntRange(1), default=10, show_default=True)
@click.argument('outfile', type=click.Path())
def main(layout, communities, colors, size, outfile):
    layout = json.load(layout)
    comm = json.load(communities)
    colors = json.load(colors)
    plot_network(layout, comm, colors, size, outfile)


if __name__ == '__main__':
    main()
