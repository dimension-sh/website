#!/usr/bin/env python3

import sys
import os
import cgi
import cgitb
cgitb.enable()

import markdown
from markdown.extensions.wikilinks import WikiLinkExtension
from jinja2 import Template


DATA_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
WIKI_ROOT = '/srv/wiki/'
BAD_CHARACTERS = ['.', '/', '\\', ' ']

with open(os.path.join(DATA_FOLDER, 'wiki_template.j2')) as fobj:
    template = Template(fobj.read())

sys.stdout.write('Content-Type: text/html\n\n')

# Get page name
qs = cgi.parse()
if 'p' in qs:
    page = qs['p'][0].lower()
else:
    page = 'index'

# Sanitize for bad filenames
for char in BAD_CHARACTERS:
    page = page.replace(char, '_')

# Check if the page exists
page_path = os.path.join(WIKI_ROOT, '%s.md' % page)
if not os.path.exists(page_path):
    page_path = os.path.join(WIKI_ROOT, '404.md')

# Open and format the page
with open(page_path, 'r') as fobj:
    page_data = fobj.read()
    html = markdown.markdown(page_data, extensions=[
                             'tables', WikiLinkExtension(base_url='/cgi/wiki.cgi?p=', end_url='')])

# Render the output
sys.stdout.write(template.render(html=html))
