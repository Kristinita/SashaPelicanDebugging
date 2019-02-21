#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sasha Chernykh'
SITENAME = 'SashaPelicanDebugging'
SITEURL = '.'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
DEFAULT_DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

DEFAULT_LANG = 'en'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'json_feed'
]

FEED_ALL_JSON = 'feeds/all.json'
CATEGORY_FEED_JSON = 'feeds/{slug}.json'

THEME = 'themes/notmyidea'

ARTICLE_PATHS = ['SashaContent']

SITEURL = '.'
