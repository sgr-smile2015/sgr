#######################################################
# $Name:         shell_template.sh
# $Version:      v1.0
# $Function:     Backup MySQL Databases Template Script
# $Author:       Jason Zhao
# $organization: https://www.unixhot.com/
# $Create Date:  2016-08-27
# $Description:  You know what i mean,hehe
#######################################################

#!/bin/bash

# Shell Env
SHELL_NAME="shell_template.sh"
SHELL_DIR="/opt/shell"
SHELL_LOG="${SHELL_DIR}/${SHELL_NAME}.log"
LOCK_FILE="/tmp/${SHELL_NAME}.lock"

#Write Log 
shell_log(){
	LOG_INFO=$1
	echo "$(date "+%Y-%m-%d") $(date "+%H-%M-%S") : ${SHELL_NAME} : ${LOG_INFO}" >> ${SHELL_LOG}

}

# Shell Usage
shell_usage(){
	echo $"Usage: $0 {backup}"

}

shell_lock(){
	touch ${LOCK_FILE}

}

shell_unlock(){
	rm -f ${LOCK_FILE}

}

# Backup MySQL All Database with mysqldump or innobackupex
mysql_backup(){
	if [ -f "$LOCK_FILE"  ];then
		shell_log "${SHELL_NAME} is running"
		echo "${SHELL_NAME}" is running && exit
	fi
	shell_log "mysql backup start"
	shell_lock
	sleep 10
	shell_log "mysql backup stop"
	shell_unlock

}

# Main Function
main(){
	case $1 in
		backup)
			mysql_backup
			;;
		*)
			shell_usage;
	esac

}

#Exec
main $1
