"""MCVE for automatically generated title metadata."""

AUTHOR = 'Sasha Chernykh'
SITENAME = 'SashaPelicanDebugging'
SITEURL = '.'

PATH = 'content'

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = 'en'

# [INFO] Use article name when preserve the slug:
# https://docs.getpelican.com/en/stable/settings.html#url-settings
SLUGIFY_SOURCE = 'basename'

# [INFO] Preserve case of article filename
SLUGIFY_PRESERVE_CASE = True

# [INFO] Get title from article filename:
# https://docs.getpelican.com/en/stable/settings.html#metadata
# https://github.com/getpelican/pelican/commit/2e82a53cdf3f1f9d66557850cc2811479d5bb645
FILENAME_METADATA = '(?P<title>.*)'
