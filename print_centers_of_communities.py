import json
import os

import click
import networkx as nx


def get_default_colors():
     directory = os.path.dirname(__file__)
     return os.path.join(directory, 'default_community_colors.json')


@click.command()
@click.argument('network', type=click.Path(exists=True, dir_okay=False))
@click.argument('communities', type=click.File('r'))
@click.option('--colors', type=click.File('r'), default=get_default_colors())
@click.argument('outfile')
def main(network, communities, colors, outfile):
    graph = nx.read_gml(network)

    colors = json.load(colors)
    comm = json.load(communities)
    in_degree = graph.in_degree()
    comm = {n: (c, in_degree[n]) for n, c in comm.items()}
    comm = {
        colors[str(c)][4:] if str(c) in colors else 'gray':
        [(n, d) for n, (c2, d) in comm.items() if c2 == c]
        for c in range(0, 9)
    }
    comm = {k: sorted(v, key=lambda x: -x[1])[:10] for k, v in comm.items()}

    for k in comm:
        print(k, comm[k])
        print()


if __name__ == '__main__':
    main()
