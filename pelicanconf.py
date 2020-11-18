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

PLUGIN_PATHS = [
    'plugins/interlinks'
]

PLUGINS = [
    'interlinks'
]

INTERLINKS = {
    'kristinita': 'https://kristinita.netlify.app/#gsc.tab=0&gsc.q='
}
