FROM centos:centos7
### Setup run parameters
EXPOSE 80
WORKDIR /home/www/app

ADD . /home/www/app/
