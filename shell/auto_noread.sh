#! /bin/bash
# ------------------------------------------------
# Filename:    auto.sh                           |
# Date:        2015/06/18                        |
# Email:       qihai.yang@gtja-trading.com               |
# ------------------------------------------------
# Copyright:   2015 (c) Sgr
# License:     GPL

#scp jvtestA@10.224.1.162:~/upload/source.tar.gz .
invok_getDirName(){
	echo "please input LOG dir.."
	read LOG
	echo "please input DATA dir.."
	read DATA
}
#invok_getDirName
LOG_DIR=$LOG
DATA_DIR=$DATA

invok_data_link(){
	cd $DATA_DIR
	mkdir data mktdata tcadata trade
	
	cd ~
	ln -s $DATA_DIR/data/ data
	ln -s $DATA_DIR/mktdata/ mktdata
	ln -s $DATA_DIR/tcadata/ tcadata
	ln -s $DATA_DIR/trade/ trade
}

invok_display(){
	LINE=$1
	i=0
	RET=3
  	 while [ $i != $RET ] ; do
      if [ $i -lt $LINE ];then
      	sleep 1
      	printf  "."
      else
     	echo " FINISHED"
     	#FOUND="1"
     	break
      fi
    let i=i+1
    done
}

invok_mkdir(){
	PRG=$1
	cd $LOG_DIR
	mkdir $PRG
		cd ~
		cd $PRG
		ln -s $LOG_DIR/$PRG/ log
		echo "log -> $LOG_DIR/$PRG/"
		ln -s ../AexLibs/ libs
	cd ~
}

invok_tca(){
	PRG=$1
	DIR=$LOG_DIR/tca
	cd $DIR
	mkdir $PRG
	cd ~/tca
		if [ -h log ] ;then 
		rm log libs
		rm *_logs *.jar > /dev/null 2>&1
		fi
	cd ~/tca
	ln -s $DIR/$PRG/ $PRG
	echo "$PRG -> $DIR/$PRG/ "
	ln -s ../AexLibs/tca.jar tca.jar > /dev/null 2>&1
	ln -s ../AexLibs/3rdparty/mail.jar mail.jar > /dev/null 2>&1
	cd ~
}

#---------------------------------------
#mail while
invok_data_link
tar -xzvf source.tar.gz  > a
awk -F / '{print $1}' a > b
awk -F / '{print $2}' a |grep logs$ > d
sort -n b | uniq > c
	LINE=`sort -n b |uniq |wc -l`
	line=0
        while read line 
        do
#        echo $line
		 if [ $line = AexLibs ] || [ $line = startall ];then	
		 echo "BEGIN..." 
		 else 
		  invok_mkdir $line
		    	row=0
		    	if [ $line = tca ] ; then
					while read row 
					do
					invok_tca $row
					done < d
					let row=row+1
				fi
          let line=line+1
		 fi
        done < c
invok_display $LINE
echo "Congratulations, please ./startall/start_all.sh Testing"
rm a b c d
