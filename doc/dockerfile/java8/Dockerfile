# IMAGE:    openjdk1.8
# VERSION:  1.0.0
# AUTHOR:   sgr

#FROM sgr0.docker.com/common/java:1.7.0
FROM openjdk:8u121-jre-alpine

MAINTAINER  openjdk <openjdk@ipin.com>

# set timezone
#RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
#	&& echo 'Asia/Shanghai' >/etc/timezone
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.3/main" >> /etc/apk/repositories && \
    apk update && apk add ca-certificates && \
    apk add tzdata && \
    apk add --no-cache bash && \
    apk add xfce4 && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone
