Title: Pelican Theme Set up
Date: 2019-08-21
Category: Pelican
Tags: Pelican-Notes


1. go into Pelican project
2. git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes
3. `pelican content -s pelicanconf.py -t ~/pelican-themes/Flex`
4. `pelican --listen`