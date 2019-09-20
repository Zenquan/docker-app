FROM daocloud.io/library/python:3.6-rc-alpine
MAINTAINER zenquan <jomsoucan@gmail.com>

RUN mkdir -p /app
WORKDIR /app

ADD requirement.txt requirement.txt
RUN pip install -r requirement.txt

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8888
ENTRYPOINT ["docker-entrypoint.sh"]
CMD [""]