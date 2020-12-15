#!/usr/bin/env bash
 
#Start cron
cron

#Start apache
/usr/sbin/apache2ctl -D FOREGROUND
