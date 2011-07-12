#!/bin/bash

TSTS=`ls test-cases | grep test`

echo "" > test.log

for x in $TSTS; do
	echo $x
	./test-cases/$x >> test.log
	ret=$?
	if [ $ret -ne 0 ]; then
		echo "  FAIL!"
	else
		echo "  OK"
	fi
done 

rm *.testdb
