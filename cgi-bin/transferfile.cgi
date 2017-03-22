#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin
filename=
getfilename() {
    for LOOP in $1
    do
        NAME=`echo $LOOP | sed 's/=/ /g' | awk '{print $1}'`
        TYPE=`echo $LOOP | sed 's/=/ /g' | awk '{print $2}' | sed 's/"/ /g' | awk '{print $1}' | sed 's/ //g' ` 
        case "$NAME" in
            "filename")
                filename="${TYPE}"               
            ;;
        esac
    done
}

savefile() {
    dd of=/tmp/test 
    nameline=`sed -n 2p /tmp/test`
    getfilename "${nameline}"
    sed -e '1,4d' -e '$d' /tmp/test  > /tmp/test.1
    rm /tmp/test
    size=`ls -l "/tmp/test.1" | awk '{ print $5 }'`
    size=`expr $size - 2`
    dd if=/tmp/test.1 of="/tmp/${filename}" bs=${size} count=1
    rm /tmp/test.1
}


savefile
printf "Content-type: text/html \n\n"
printf "/tmp/$filename"
