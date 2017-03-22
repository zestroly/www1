#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin
echo -e "Content-type:text/html \n\n"
read temp


parameter=`echo $temp | tr " \t\n" " " | awk -F: '{print $2}'`
parameter=`echo $parameter | tr -d " " `
head=`echo $temp | tr " \t\n" " " | awk -F: '{print $1}'`

function Switch(){
	step1=`/opt/bin/printshmcgi $parameter`
#	step1=`/opt/kzh/202/printshmcgi/printshmcgi $parameter`
	echo $step1
#	echo 22 > tttt
}

function BaseInformation(){
	step1=`/opt/bin/printshmcgi $parameter`
	echo $step1
}

function FaultInformation(){
	step1=`/opt/bin/printshmcgi $parameter`
	echo $step1
}

function BatteryInformation(){
	step1=`/opt/bin/printshmcgi $parameter`
	echo $step1
}

function PressInformation(){
	step1=`/opt/bin/printshmcgi $parameter`
	echo $step1
}

function Others(){
	step1=`/opt/bin/printshmcgi $parameter`
	echo $step1
	#echo $temp > tttt
}

if [ "$parameter" = "开关信息" ]
then
	Switch
elif [ "$parameter" = "车辆基本信息" ]
then
	BaseInformation
elif [ "$parameter" = "故障信息" ]
then
	FaultInformation
elif [ "$parameter" = "电池单体信息" ]
then
	BatteryInformation
elif [ "$parameter" = "胎压信息" ]
then
	PressInformation
elif [ "$parameter" = "其它模块" ]
then
	Others
fi
