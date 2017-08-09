#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
#dossier avec les articles
content = u"/home/valerian/vfreysz@gmail.com/Python_Git/site_web/vfreysz.github.io-src/content"

#tab avec les liens vers les differents notebook
link_to_jupyter_notebook = []
link_to_jupyter_notebook.append(u"/home/valerian/vfreysz@gmail.com/Python_Git/Equilibre_Thermo/Equilibre_thermodynamique.ipynb")

#copy de tous les notebook dans le dossier du blog
for link in link_to_jupyter_notebook:
    shutil.copy(link, content)


pelicanconf = "/home/valerian/vfreysz@gmail.com/Python_Git/site_web/vfreysz.github.io-src/pelicanconf.py"
#construction du site

from fabric.api import run
commande = ' pelican ' + content + ' -s ' + pelicanconf
run(commande)