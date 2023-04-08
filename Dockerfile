# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers supervisor nginx
COPY supervisord.conf /etc/supervisord.conf
COPY requirements.txt requirements.txt
COPY nginx.conf /etc/nginx/nginx.conf
COPY proxy_params /etc/nginx/proxy_params
RUN pip install -r requirements.txt
EXPOSE 80
COPY . .
RUN mkdir -p /var/log/supervisor
CMD ["/usr/bin/supervisord"]
