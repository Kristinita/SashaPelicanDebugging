#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sasha Chernykh'
SITENAME = 'SashaPelicanDebugging'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
DEFAULT_DATE_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'loadcsv'
]

THEME = 'themes/notmyidea'

# filetime_from_git
# https://github.com/getpelican/pelican-plugins/tree/master/filetime_from_git#other-options
GIT_HISTORY_FOLLOWS_RENAME = True
GIT_GENERATE_PERMALINK = True
GIT_SHA_METADATA = True
GIT_FILETIME_FROM_GIT = True

ARTICLE_PATHS = ['SashaContent']

SITEURL = '.'
