#!/usr/bin/env python3
import sys
from twtxt.parser import parse_tweets

sys.stdout.write('Content-Type: text/html\n\n')

with open('/srv/news/patchlog.txt', 'r') as fobj:
    tweets = parse_tweets(fobj.readlines(), 'patchlog')

sys.stdout.write("<div id='patchlog'>")
for tweet in sorted(tweets, key=lambda: x: x.created_at, reverse=True)[:10]:
    sys.stdout.write(f"<div class='patchentry'><b id='date'>{tweet.created_at.date()}</b><p>{tweet.text}</p></div>")
sys.stdout.write("</div>")
