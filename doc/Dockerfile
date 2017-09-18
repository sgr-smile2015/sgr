FROM node:7-alpine  
LABEL maintainer "alpine@163.com"

ENV PROJECT_DIR=/app  
WORKDIR $PROJECT_DIR

COPY package.json $PROJECT_DIR  
RUN npm install  
COPY . $PROJECT_DIR

ENV MEDIA_DIR=/media \  
    NODE_ENV=production \
    APP_PORT=3000

VOLUME $MEDIA_DIR  
EXPOSE $APP_PORT  

HEALTHCHECK CMD curl --fail http://localhost:$APP_PORT || exit 1

CMD ["npm", "start"]
