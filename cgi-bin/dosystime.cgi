#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin
POSTSTRING=
day=
time=
getinputvalue() {
    LINE=`echo $POSTSTRING | sed 's/&/ /g'`
    for LOOP in $LINE
    do
        NAME=`echo $LOOP | sed 's/=/ /g' | awk '{print $1}'`
        TYPE=`echo $LOOP | sed 's/=/ /g' | awk '{print $2}' | sed 's/+/ /g' | sed 's/%2F/\//g' | sed 's/%3A/:/g' ` 
        case "$NAME" in
            "day")
                day="${TYPE}"
            ;;
            "time")
                time="${TYPE}"
            ;;
        esac
            
    done

}


POSTSTRING=`cat -`
echo  -e "Content-type: text/html \n\n"
echo "<html>"
echo "<head>"
echo "<title>时间设置</title>"
echo "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />"
echo "</head>"
echo "<body>"
echo "<center>"
echo "<h3>系统时间设置</h3>"
echo "</center>"
echo "<hr>"
    getinputvalue
    TIMESTRING="${day} ${time}"
    date -s "${TIMESTRING}" > /dev/null
    hwclock -w > /dev/null
    echo "<br><br>"
    echo "设置成功"
echo "</body>"
echo "</html>"

