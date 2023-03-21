import click
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import dates


@click.command()
@click.argument('infile')
@click.argument('outfile')
@click.option('--xlocator', default=7, show_default=True)
def main(infile, outfile, xlocator):
    counts = pd.read_csv(infile)
    granularity = counts.columns[-1].split('_')[0]
    y = granularity + '_count'
    counts['start'] = counts['start'].apply(lambda x: x[:10])
    counts = counts.sort_values(['start', y], ascending=False)
    if 'query' in counts.columns:
        ax = sns.lineplot(data=counts, x='start', y=y, hue='query')
    else:
        ax = sns.lineplot(data=counts, x='start', y=y)
    ax.xaxis.set_major_locator(dates.DayLocator(interval=xlocator))
    plt.xticks(rotation=90)
    plt.xlabel(granularity)
    plt.ylabel('tweets')
    plt.tight_layout()
    ax.get_figure().savefig(outfile)


if __name__ == '__main__':
    main()
