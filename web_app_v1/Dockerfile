FROM ubuntu

MAINTAINER Anoop Macharla <149@holbertonschool.com>

# Install MySQL 5.7
RUN apt-get -y update
RUN echo "mysql-server-5.7 mysql-server/root_password password r00t" | debconf-set-selections
RUN echo "mysql-server-5.7 mysql-server/root_password_again password r00t" | debconf-set-selections
RUN apt-get -y install mysql-server

# Install supporting lib for MySQLdb for python3.5
RUN apt-get -y install python3-dev
RUN apt-get -y install libmysqlclient-dev
RUN apt-get -y install zlib1g-dev
RUN apt-get -y install python3-pip

# Install Nginx ----
RUN apt-get -y install nginx

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

# tell the container what port will be using 
EXPOSE 80 3306

# Make NGINX run on the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# configs
#COPY config_files/uwsgi_config.ini /var/www/url_shortener/web_app/

# Remove default configuration from Nginx and add custom
#COPY config_files/nginx_site /etc/nginx/sites-available/
RUN ln -fs /etc/nginx/sites-available/nginx_site /etc/nginx/sites-enabled/default

# Move respective files to right location based on configration
# copy web_app to /var/www/url_shortener/
RUN mkdir -p /var/www/url_shortener/
COPY web_app /var/www/url_shortener/web_app

#python requirements
COPY config_files/requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt \
	&& rm -rf /requirements.txt

CMD ["service mysql start"]

#DB setup 
COPY config_files/dbsetup.sh /db_setup.sh
CMD ["~/./dbsetup.sh url_db"]
RUN rm -rf /dbsetup.sh


CMD ["/usr/sbin/nginx"]
CMD ["/usr/local/bin/uwsgi --ini /var/www/url_shortener/web_app/uwsgi_config.ini"]
