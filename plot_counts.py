import click
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import dates


@click.command()
@click.argument('infile')
@click.argument('outfile')
def main(infile, outfile):
    counts = pd.read_csv(infile)
    counts['start'] = counts['start'].apply(lambda x: x[:10])
    counts = counts.sort_values(['start', 'query'], ascending=False)
    ax = sns.lineplot(data=counts, x='start', y='day_count', hue='query')
    ax.xaxis.set_major_locator(dates.DayLocator(interval=7))
    plt.xticks(rotation=90)
    plt.xlabel('day')
    plt.ylabel('tweets')
    plt.tight_layout()
    ax.get_figure().savefig(outfile)


if __name__ == '__main__':
    main()
