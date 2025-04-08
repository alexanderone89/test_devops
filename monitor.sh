#!/bin/bash

servicetorun=0;

while true
do
    d=$(date +%d-%m-%Y__%H:%M:%S);
#  if [ -z "$(ps -C test --no-headers)" ];
   if [ -z "$(ps -ef | grep -i '[t]est')" ];
      then
      {
        echo "TEST NO RUN" >> /var/log/monitoring.log ;
        servicetorun=1;
      }
      else
      {
        if [ "$servicetorun" -eq "1" ]
          then
            echo "[ $d ] TEST TO REBOOT" >> /var/log/monitoring.log ;
            servicetorun=0;
        fi
#        echo 'TEST IS RUN';
        resp_code=$(curl -s -w "%{http_code}\n" -L  "http://localhost:8000/monitoring/test/api?arm=1&sign=1" -o /dev/null)
        if [ "$resp_code" -eq "000" ]
          then
            echo "[ $d ] SERVER UNREACHABLE" >> /var/log/monitoring.log;
          fi
#        curl  -X POST "http://localhost:8000/monitoring/test/api?arm=1&sign=1";
      }
    fi
  sleep 1s
done
