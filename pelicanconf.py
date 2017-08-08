#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals



AUTHOR = 'Valerian FREYSZ'
SITENAME = 'ValsBlog'
SITEURL = ''
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = 	(('github', 'https://github.com/vfreysz'),
		('linkedin', 'https://www.linkedin.com/in/valerian-freysz'),)


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#Plugin
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['ipynb.markup']
#PLUGINS = ['pelican-ipynb.markup','i18n_subsites']

#Ipython notebook
#MARKUP = ('md', )
MARKUP = ('md', 'ipynb')
IPYNB_IGNORE_CSS = True


#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

#THEME = u'../pelican-themes/pelican-bootstrap3'
#THEME = u'../pelican-themes/SoMA'
#THEME = u'../pelican-themes_git/pelican-pure'
#THEME = u'../pelican-themes_git/pure-single'
THEME = u'../pelican-themes_git/pure'
PROFILE_IMG_URL = u'photo/photo_nb_large.jpg'
COVER_IMG_URL = u'photo/Side_image_ld.jpg'




