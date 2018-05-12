#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tony Locke'
SITENAME = 'Tony Locke'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('MtrHub', 'http://www.mtrhub.com/'),
    (
        'My Glimpse Inside The Ivory Tower Of Mathematics',
        'http://maths.tlocke.org.uk/'),
    ('Polifesto', 'http://www.polifesto.com/'),
    (
        'La Licorne Manifesto',
        'http://www.polifesto.com/view_policy?'
        'policy_key=ag9zfnBvbGlmZXN0by1ocmRyDgsSBlBvbGljeSICcDEM'),)

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/t_locke'),
    ('GitHub', 'https://github.com/tlocke'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

OUTPUT_PATH = 'docs'
THEME = "/home/tlocke/home/themes/notmyidea"
