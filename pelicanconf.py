#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brice OLIVIER'
SITENAME = u'Brice OLIVIER'  # lekiduckhasz.github.io
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['documents']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Inria, Mistis', 'https://mistis.inrialpes.fr/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/brice-olivier-47831272'),
          ('github', 'https://github.com/brice-olivier'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/pelican-blue'
# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['linker', 'pdf-img']
AVATAR = './documents/profile_picture.jpg'
SIDEBAR_DIGEST = 'PhD student at the University of Grenoble Alpes, France'
EMAIL1 = 'briceolivier1409@gmail.com'
EMAIL2 = 'brice.olivier@inria.fr'

# FAVICON = 'url-to-favicon'

DISPLAY_PAGES_ON_MENU = True

# TWITTER_USERNAME = 'LekiDuckHasz'

ARTICLE_ORDER_BY = 'order_id'
PAGE_ORDER_BY = 'order_id'
