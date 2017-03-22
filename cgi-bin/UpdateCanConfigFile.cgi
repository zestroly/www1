#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin
echo -e "Content-type:text/html \n\n"
read temp

cd /opt/bin
killall *
killall *
filetype=`echo ${temp#*.}`
if [ "$filetype" = "zip" ];then
	unzip -o $temp -d /opt/config >/dev/null 2>&1
	if [ $? -ne 0 ];then
		echo "升级失败"
		exit
	fi
elif [ "$filetype" = "tar.gz" ];then
	tar xvf $temp -C /opt/config >/dev/null 2>&1
	if [ $? -ne 0 ];then
		echo "升级失败"
		exit
	fi
elif [ "$filetype" = "tar" ];then
	tar xvf $temp -C /opt/config >/dev/null 2>&1
	if [ $? -ne 0 ];then
		echo "升级失败"
		exit
	fi
else
	cp -rf $temp /opt/config >/dev/null 2>&1
	if [ $? -ne 0 ];then
		echo "升级失败"           
        exit
	fi
fi
chmod -R 777 /opt/config
if [ $? -ne 0 ];then
	echo "添加权限失败"
	exit
fi

echo "升级成功"
#sleep 1
reboot
