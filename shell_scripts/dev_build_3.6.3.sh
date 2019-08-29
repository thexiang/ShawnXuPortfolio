source dev/bin/activate
pelican content -s pelicanconf.py -t theme/sx_portfolio_theme
cd /Users/xiang/Desktop/Portfolio/output/
python -m pelican.server