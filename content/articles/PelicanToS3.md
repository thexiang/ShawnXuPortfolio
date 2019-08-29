Title: Pelican to S3
Date: 2019-08-11
Category: Notes
Tags: Pelican-Notes


1. set up pelican
2. create a aws user from IAM, grant it admin
3. pip install awscli
4. aws configure
5. login with user's access key
6. create s3 bucket, set it public
7. aws s3 cp output/ s3://shawnxuportfolio/ --recursive

Step by Step Details:
http://anendeavour.com/hosting_a_static_blog_on_s3.html