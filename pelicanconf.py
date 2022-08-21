"""MCVE."""

AUTHOR = 'Sasha Chernykh'
SITENAME = 'SashaPelicanDebugging'
SITEURL = 'https://kristinita.netlify.app'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

ARTICLE_PATHS = [
    'Articles'
]

PLUGINS = ['pelican-search']

MARKDOWN = {
    'output_format': 'html5',
}
