#! /bin/bash
# the scripts use to delete docker images's tag is <none>
#touch by 2016.07.19

imageID=`sudo docker images |grep "<none>" |awk '{print $3}'`
containerID=`sudo docker ps -a |grep "${imageID}" |awk '{print $1}'`

sudo docker stop ${containerID}
sudo docker rm ${containerID}
sudo docker rmi ${imageID}
