source dev/bin/activate
pelican content -s pelicanconf.py -t theme/sx_portfolio_thme
aws s3 cp output/ s3://shawnxuportfolio/ --recursive