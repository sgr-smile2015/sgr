#!/bin/sh
# Jenkins Build Shell Script
# Author zdzhou@iflytek.com

set -e 
# Get running docker image name
cid=`docker ps | grep 'isearch' | awk {'print $1'}`
echo $cid

# If exists running isearch docker image, stop and remove it
if [ -n "$cid" ]
then
    echo Get the running docker container id of isearch: $cid
    docker stop $cid
    docker rm $cid
else  
    echo There is no running isearch docker container
fi

# Copy target war to dest directory
cd ${JENKINS_HOME}/workspace/${JOB_NAME}/itv-web/
echo Current work directory `pwd`
cp target/itv-web.war /usr/local/tomcat/webapps
echo Run docker image
docker run -d -p 8080:8080 -v /usr/local/isearch:/usr/local/isearch -v /usr/local/tomcat/webapps:/usr/local/tomcat/webapps --name=isearch${SVN_REVISION} isearch

# Wait for starting docker container
totalWait=0
until [ "`/usr/bin/docker inspect -f {{.State.Running}} isearch${SVN_REVISION}`" == "true" ] 
do
   totalWait=$[ $totalWait + 2 ]
   if (( $totalWait > 10 ))
   then
      echo "Start docker container timeout"
      exit 1
   fi
   echo "Waiting for starting docker container: $totalWait minute" 
   sleep 2m
done
echo "Start docker container success "

# Wait for starting tomcat
totalWait=0
until [ "`curl -o /dev/null --silent -m 10 --retry 1 --connect-timeout 10 --head --write-out '%{http_code}\n' http://127.0.0.1:8080/itv-web/v3/videosearch/?appid=aginomoto`" = "200" ]
do 
  totalWait=$[ $totalWait + 3 ]
  if (($totalWait > 36 ))
  then 
    echo "Start tomcat timeout"
    exit 1
  fi
  echo "Wait for starting tomcat: "$totalWait" minute"
  sleep 3m
done 
echo "Start tomcat service success"

# Run automatic function test script
echo "Start automatic function test"
export LOG_HOME=${WORKSPACE}/test.log.d/${BUILD_NUMBER}
cd /data/jenkins_home/test.framework.d
exec ./automatic_test.sh 
