#!/usr/bin/env python3
imprt sys
from twtxt.parser import parse_tweets

sys.stdout.write('Content-Type: text/html\n\n')

with open('/srv/news/patchlog.txt', 'r') as fobj:
    tweets = parse_tweets(fobj.readlines(), 'patchlog')

sys.stdout.write("<div id='patchlog'>'")
for tweet in tweets:
    sys.stdout.write(f"<div class='patchentry'><span id='date'>{tweet.created_at.date()}</span> - {tweet.text}</div>")
sys.stdout.write("</div>")
