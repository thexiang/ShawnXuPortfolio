#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shawn Xu'
SITENAME = "Shawn Xu's Portfolio"
SITEURL = ''
PORT = 8111
PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'


SOCIAL = (
    ('github', 'https://github.com/thexiang'),
)

MENUITEMS = (
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),
             ('Archives', '/archives.html'),
             )

DEFAULT_PAGINATION = False

MAIN_MENU = True

STATIC_PATHS = ['images', 'extra']
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PYGMENTS_STYLE = 'abap'


DATE_FORMATS = {
    'en': '%m/%d/%Y',
}


ARTICLE_PATHS = ['articles','python','Python Data Science', 'Python OOP']
# ARTICLE_PATHS = ['python']

# Path to the folder containing the plugins
PLUGIN_PATHS = ['pelican-plugins']
# Enabled plugins
PLUGINS = ['pelican-ipynb.markup']

MARKUP = ('md', 'ipynb')

IGNORE_FILES = [".ipynb_checkpoints"]  

IPYNB_USE_METACELL = True

GOOGLE_ANALYTICS = "UA-147516390-1"