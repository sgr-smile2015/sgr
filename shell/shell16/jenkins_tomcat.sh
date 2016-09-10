#!/bin/bash
#defined

TOMCAT_HOME="/save/apache-tomcat-7.0.56"  
TOMCAT_PORT=8080  
PROJECT="$1"  
#param validate  
if [ $# -lt 1 ]; then    
  echo "you must use like this : ./publish.sh <projectname> [tomcat port] [tomcat home dir]"    
  exit    
fi   
if [ "$2" != "" ]; then  
   TOMCAT_PORT=$2  
fi  
if [ "$3" != "" ]; then  
   TOMCAT_HOME="$3"  
fi  
#shutdown tomcat  
"$TOMCAT_HOME"/bin/shutdown.sh  
echo "tomcat shutdown"  
#check tomcat process  
tomcat_pid=`/usr/sbin/lsof -n -P -t -i :$TOMCAT_PORT`  
echo "current :" $tomcat_pid  
while [ -n "$tomcat_pid" ]  
do  
 sleep 5  
 tomcat_pid=`/usr/sbin/lsof -n -P -t -i :$TOMCAT_PORT`  
 echo "scan tomcat pid :" $tomcat_pid  
done  
#publish project  
echo "scan no tomcat pid,$PROJECT publishing"  
rm -rf "$TOMCAT_HOME"/webapps/$PROJECT*  
cp /save/$PROJECT*.war "$TOMCAT_HOME"/webapps/$PROJECT.war  
#bak project  
BAK_DIR=/save/bak/$PROJECT/`date +%Y%m%d`  
mkdir -p "$BAK_DIR"  
cp "$TOMCAT_HOME"/webapps/$PROJECT.war "$BAK_DIR"/"$PROJECT"_`date +%H%M%S`.war  
#remove tmp  
rm -rf /save/$PROJECT*.war  
#start tomcat  
"$TOMCAT_HOME"/bin/startup.sh  
echo "tomcat is starting,please try to access $PROJECT conslone url"  
