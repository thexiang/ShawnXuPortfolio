#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shawn Xu'
SITENAME = "Shawn Xu's Portfolio"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (
    ('github', 'https://github.com/thexiang'),
)

MENUITEMS = (('Blog', '/'),
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = False

MAIN_MENU = True

STATIC_PATHS = ['images', 'extra']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PYGMENTS_STYLE = 'borland'


DATE_FORMATS = {
    'en': '%m/%d/%Y',
}


ARTICLE_PATHS = ['articles','articles/test']