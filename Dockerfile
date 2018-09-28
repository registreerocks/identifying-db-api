#This API is used to store student information within a mongodb. 
# An nginx server is used as a reverse proxy for the the Swagger/Flask
# API managed using Gunicorn, via Supervisord.

FROM python:3.6

#SSL
# RUN openssl req \
#     -new \
#     -newkey rsa:4096 \
#     -days 365 \
#     -nodes \
#     -x509 \
#     -subj "/C=ZA/ST=WC/L=CapeTown/O=Registree/CN=www.registree.rocks" \
#     -keyout server.key \
#     -out server.cert

# connexion
RUN mkdir -p /usr/src
COPY oas3.zip /usr/src
WORKDIR /usr/src

RUN  apt-get update -y && \
     apt-get upgrade -y && \
     apt-get install unzip -y 

RUN unzip oas3.zip
RUN mv connexion-oas3 connexion
WORKDIR connexion
RUN pip install -e .

# API
RUN mkdir -p /usr/src/package
COPY ./package /usr/src/package
WORKDIR /usr/src/package
RUN pip install -e .

# Deployment
# RUN apt-get install nginx supervisor -y
RUN apt-get install supervisor -y
RUN pip install gunicorn


# Supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# EXPOSE 8080

# Start processes
CMD ["/usr/bin/supervisord"]