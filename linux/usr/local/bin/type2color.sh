#!/bin/sh

screen -DmS type2color bash -c "/usr/bin/python3 /usr/local/bin/type2color.py"
ret=$?

exit $ret
