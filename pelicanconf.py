"""MCVE."""

# [INFO] Default settings
AUTHOR = 'Sasha Chernykh'
SITENAME = 'SashaPelicanDebugging'
SITEURL = 'https://kristinita.netlify.app'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

ARTICLE_PATHS = [
    'Articles'
]

MARKDOWN = {
    'output_format': 'html5',
}


# [INFO] Settings for issue
PLUGINS = [
    'search'
]

SEARCH_HTML_SELECTOR = "body"

OUTPUT_PATH = 'output'
