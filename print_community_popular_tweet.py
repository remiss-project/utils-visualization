import json
import os
from collections import Counter

import click
from tqdm import tqdm
from twarc import ensure_flattened


def is_retweet(tweet):
    try:
        if tweet['referenced_tweets'][0]['type'] == 'retweeted':
            return True
        else:
            return False
    except Exception:
        return False


@click.command()
@click.argument('communities', type=click.File('r'))
@click.argument('tweets', type=click.File('r'))
@click.option('-n', default=10, show_default=True)
@click.argument('outfile', type=click.File('w'))
def main(communities, tweets, n, outfile):
    comm = json.load(communities)
    tweet = {c: None for c in range(n)}
    retweets = {c: 0 for c in range(n)}
    with tqdm(total=os.stat(tweets.name).st_size, unit='B') as progress:
        for line in tweets:
            for t in ensure_flattened(json.loads(line)):
                if is_retweet(t):
                    continue
                user = t['author']['username']
                if user not in comm:
                    continue
                c = comm[user]
                if c >= n:
                    continue
                if t['public_metrics']['retweet_count'] > retweets[c]:
                    retweets[c] = t['public_metrics']['retweet_count']
                    tweet[c] = user + ': ' + t['text']
            progress.update(len(line))

    for c, t in tweet.items():
        outfile.write(str(c) + '\t' + t.replace('\n', '\\n') + '\n\n')


if __name__ == '__main__':
    main()
