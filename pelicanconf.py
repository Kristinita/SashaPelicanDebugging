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
PLUGIN_PATHS = [
    'pelican-plugins'
]

SEARCH_HTML_SELECTOR = "body"

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}
