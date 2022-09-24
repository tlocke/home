#!/usr/bin/env python

AUTHOR = "Tony Locke"
SITENAME = "Tony Locke"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_DOMAIN = "https://www.tlocke.org.uk"
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = None

# Social widget
SOCIAL = None
DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ("Archive", "/archives.html"),
    ("GitHub", "https://github.com/tlocke"),
)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

OUTPUT_PATH = "docs"
# THEME = "/home/tlocke/home/themes/notmyidea"
THEME = "themes/simple"
YEAR_ARCHIVE_SAVE_AS = "posts/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "posts/{date:%Y}/{date:%b}/index.html"
DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "period_archives")

STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

READERS = {"html": None}
