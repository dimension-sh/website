#!/usr/bin/env python3

import sys
import os
import cgi
import cgitb
import glob
from datetime import datetime

from jinja2 import Template
from markdown.extensions.wikilinks import WikiLinkExtension
import markdown
import frontmatter

cgitb.enable()


DATA_FOLDER = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data'))
NEWS_ROOT = '/srv/news/'
MAX_NEWS_ARTICLES = 5


def parse_markdown(page_data):
    extensions = [
        'tables',
        'fenced_code',
    ]
    return markdown.markdown(page_data, extensions=extensions)


if __name__ == '__main__':
    sys.stdout.write('Content-Type: text/html\n\n')

    with open(os.path.join(DATA_FOLDER, 'news_template.j2'), 'r') as fobj:
        news_template = Template(fobj.read())

    html = ''
    filenames = glob.glob(os.path.join(NEWS_ROOT, '*.md'))
    filenames.sort(reverse=True)
    for filename in filenames[:MAX_NEWS_ARTICLES]:
        with open(filename, 'r') as fobj:
            post = frontmatter.load(fobj)
        rendered = parse_markdown(post.content)
        html += news_template.render(post=post, rendered_post=rendered)

    # Render the output
    with open(os.path.join(DATA_FOLDER, 'wiki_template.j2')) as fobj:
        template = Template(fobj.read())
    sys.stdout.write(template.render(html=html))