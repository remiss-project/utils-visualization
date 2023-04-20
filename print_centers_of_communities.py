import json

import click
import networkx as nx


def int_to_color(x, colors):
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
@click.argument('network')
@click.argument('communities')
@click.option('--colors', default=None)
@click.argument('outfile')
def main(network, communities, colors, outfile):
    graph = nx.read_gml(network)

    with open(communities) as f:
        comm = json.load(f)
    in_degree = graph.in_degree()
    comm = {n: (c, in_degree[n]) for n, c in comm.items()}
    comm = {
        int_to_color(c, colors)[4:]:
        [(n, d) for n, (c2, d) in comm.items() if c2 == c]
        for c in range(0, 9)
    }
    comm = {k: sorted(v, key=lambda x: -x[1])[:10] for k, v in comm.items()}

    for k in comm:
        print(k, comm[k])
        print()


if __name__ == '__main__':
    main()
