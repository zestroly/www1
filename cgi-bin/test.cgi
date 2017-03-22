#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin
filepath="/opt/config/commu.conf"
getinfo(){
    cat $filepath | tr -d " \t" | sed "s/\(.*\)=\(.*\)#\(.*\)/\1:{\"\2\":\"\3\"},/g;1 i ({" | sed  "$ a })" | tr "\n" " "
}
echo  -e "Content-type: text/html \n\n"
read temp
filename=`echo ${temp%%&*} | tr -s "=" " " | awk '{print $2}'`
buf=${temp#*&}

cmdtype=`echo ${buf%%&*} | tr -s "=" " " | awk '{print $2}'`
if [ "$filename" == "commu" ];then
    filepath="/opt/config/commu.conf"
elif [ "$filename" == "state" ];then
    filepath="/opt/config/state.conf"
fi

if [ "$cmdtype" == "read" ];then
    getinfo
elif [ "$cmdtype" == "write" ];then
    echo ${buf#*&} > $filepath
    sed -i 's/&/\n/g' $filepath
    getinfo
else
    echo "Error"
fi
