#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin
checkip() {
    if [[ "$1" = "" ]];then
        return 1
    fi
    
    if [[ "$1" = "0.0.0.0" ]];then
        return 1
    fi
    
    a=`echo "$1" | awk -F. '{print $1}'`
    b=`echo "$1" | awk -F. '{print $2}'`
    c=`echo "$1" | awk -F. '{print $3}'`
    d=`echo "$1" | awk -F. '{print $4}'`
    if [ "$a" = "" ] || [ "$b" = "" ] || [ "$c" = "" ] || [ "$d" = "" ];then
        return 1
    fi
    for loop in $a $b $c $d
    do
        if [ ${loop} -ge 255 ] || [ ${loop} -le 0 ]; then
            return 1
        fi
    done
    return 0
}

checknetmask() {
    if [[ $1 = "" ]];then
        return 1
    fi
    if [ $1 -ge 32 ] || [ $1 -le 0 ]; then
        return 1
    fi
    return 0
}


checkinput() {
    checkip "${ipaddr}"
    if [ $? -eq 1  ];then
        echo "IP地址格式错误"
        return 1
    fi
    checkip "${gateway}"
    if [  $? -eq 1 ];then
        echo "网关地址格式错误"
        return 1
    fi
    checknetmask "${netmask}"
    if [ $? -eq 1 ];then
        echo "子网掩码格式错误"
        return 1
    fi
    return 0
}

seteeprom() {
    eeprom net set ip "${ipaddr}"
    if [ $? -ne 0 ]; then
        echo "设置 IP 地址错误"
        return 1
    fi
    eeprom net set netmask "${netmask}"
    if [ $? -ne 0 ]; then
        echo "设置子网掩码错误"
        return 1
    fi
    eeprom net set gateway "${gateway}"
    if [ $? -ne 0 ]; then
        echo "设置网关地址错误"
        return 1
    fi
    return 0
}

ipaddr=
netmask=
gateway=
echo  -e "Content-type: text/html \n\n"
echo "<html>"
echo "<head>"
echo "<title>网络设置</title>"
echo "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />"
echo "</head>"
echo "<body>"
echo "<center>"
echo "<h3>网络设置</h3>"
echo "</center>"
echo "<hr>"
if [ "$REQUEST_METHOD" = "POST" ] ; then
    QUERY_STRING=`cat -`
fi

LINE=`echo $QUERY_STRING | sed 's/&/ /g'`
for LOOP in $LINE
do
    NAME=`echo $LOOP | sed 's/=/ /g' | awk '{print $1}'`
    TYPE=`echo $LOOP | sed 's/=/ /g' | awk '{print $2}' | sed -e 's/%\(\)/\\x/g' | sed 's/+/ /g'`
    case $NAME in
        "ipaddr")
            ipaddr="${TYPE}"
        ;;
        "netmask")
            netmask="${TYPE}"
        ;;
        "gateway")
            gateway="${TYPE}"
        ;;
    esac
done
checkinput
if [ $? -eq 0 ];then
    seteeprom
    if [ $? -eq 0 ]; then
        echo "设置成功"
    fi
fi
echo "</body>"
echo -e "</html>\n\n"
 
