#!/bin/bash
cores=""
echo "Before grepping" $echo
echo $cores;

while ["$cores" = "" ]
do
    sleep 1
    cores=$(grep tanvir /homes/tkekan/PR/889083/withdebug/grab_20140916_235324/bru1/var/log/messages)
    echo "grepped is " $cores
done

