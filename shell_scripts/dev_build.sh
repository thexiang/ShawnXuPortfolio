cd theme/sx_portfolio_theme
node_modules/gulp/bin/gulp.js default
cd ..
cd ..
pelican content -s pelicanconf.py -t theme/sx_portfolio_theme
pelican --listen