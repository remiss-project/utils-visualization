import json
from collections import Counter

import click
import matplotlib.pyplot as plt


@click.command()
@click.argument('communities', type=click.File('r'))
@click.option('-n', default=10, show_default=True)
@click.argument('outfile', type=click.Path())
def main(communities, n, outfile):
    comm = json.load(communities).values()
    counts = Counter(comm).most_common(n)
    x = [x for x, _ in counts]
    y = [y for _, y in counts]

    plt.clf()
    fig = plt.figure()
    plt.bar(x, y)
    plt.xlabel('Community')
    plt.ylabel('Number of users')
    plt.tight_layout()
    fig.savefig(outfile)
    plt.close()


if __name__ == '__main__':
    main()
