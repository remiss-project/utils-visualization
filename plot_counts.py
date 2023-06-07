import click
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import dates


@click.command()
@click.argument('infile', type=click.File('r'))
@click.argument('outfile', type=click.Path())
@click.option('--xlocator', default=7, show_default=True)
@click.option('--group', is_flag=True)
@click.option('--ylabel', default='tweets', show_default=True)
def main(infile, outfile, xlocator, group, ylabel):
    counts = pd.read_csv(infile)
    granularity = counts.columns[-1].split('_')[0]
    y = granularity + '_count'
    counts['start'] = counts['start'].apply(lambda x: x[:10])
    counts = counts.sort_values(['start', y], ascending=[True, False])
    if counts.columns[0] != 'start' and not group:
        ax = sns.lineplot(data=counts, x='start', y=y, hue=counts.columns[0])
    else:
        counts = counts[['start', y]].groupby('start').sum()
        ax = sns.lineplot(data=counts, x='start', y=y)
    ax.xaxis.set_major_locator(dates.DayLocator(interval=xlocator))
    plt.xticks(rotation=90)
    plt.xlabel(granularity)
    plt.ylabel(ylabel)
    plt.tight_layout()
    ax.get_figure().savefig(outfile)


if __name__ == '__main__':
    main()
