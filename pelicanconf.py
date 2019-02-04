#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sasha Chernykh'
SITENAME = 'SashaPelicanDebugging'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
DEFAULT_DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'pelican-open_graph'
]

THEME = 'themes/notmyidea'

ARTICLE_PATHS = ['SashaContent']

SITEURL = '.'
