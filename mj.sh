#!/bin/bash

var=$(echo $PWD | awk -F '/' '{print $4}')
cd /b/tkekan/$var/src
mk -j12 jkernel
